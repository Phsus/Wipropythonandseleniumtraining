from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/')
def health_check():
    return "<h1>Healthcare API (v1) is Running!</h1><p>Use Postman with Bearer Token to test.</p>", 200



data_store = {
    "doctors": {},
    "patients": {},
    "appointments": {},
    "doctor_id_counter": 501,
    "patient_id_counter": 101,
    "appointment_id_counter": 1001
}

VALID_TOKEN = "qa-senior-token-123"



def check_auth():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {VALID_TOKEN}":
        return False
    return True


#  ROUND 1: Doctor Creation & Patient Registration

@app.route('/v1/doctors', methods=['POST'])
def create_doctor():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    doc_id = data_store["doctor_id_counter"]
    data_store["doctors"][doc_id] = data
    data_store["doctor_id_counter"] += 1

    return jsonify({"doctor_id": doc_id, "status": "201 Created"}), 201


@app.route('/v1/patients', methods=['POST'])
def register_patient():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    # Edge Case: Missing Email
    if 'email' not in data:
        return jsonify({"error": "Missing email"}), 400

    # Edge Case: Invalid Age
    if data.get('age', 0) < 0:
        return jsonify({"error": "Invalid age"}), 400

    # Edge Case: Duplicate Phone
    for p in data_store["patients"].values():
        if p.get('phone') == data.get('phone'):
            return jsonify({"error": "Conflict: Duplicate phone number"}), 409

    p_id = data_store["patient_id_counter"]
    data_store["patients"][p_id] = data
    data_store["patient_id_counter"] += 1

    return jsonify({"patient_id": p_id}), 201


# ROUND 2 & 3: Appointment Booking & Rescheduling

@app.route('/v1/appointments', methods=['POST'])
def book_appointment():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    # Check if slot is available
    for appt in data_store["appointments"].values():
        if (appt['doctor_id'] == data['doctor_id'] and
                appt['date'] == data['date'] and
                appt['time'] == data['time']):
            return jsonify({"error": "Conflict: Time slot already booked"}), 409

    a_id = data_store["appointment_id_counter"]
    data_store["appointments"][a_id] = data
    data_store["appointment_id_counter"] += 1

    return jsonify({"appointment_id": a_id, "message": "Booked"}), 201


@app.route('/v1/appointments/<int:id>', methods=['PUT'])
def reschedule_appointment(id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if id not in data_store["appointments"]:
        return jsonify({"error": "Appointment not found"}), 404

    data = request.json
    # Check if new time slot is booked by someone else
    for app_id, appt in data_store["appointments"].items():
        if (app_id != id and
                appt['doctor_id'] == data['doctor_id'] and
                appt['date'] == data['date'] and
                appt['time'] == data['time']):
            return jsonify({"error": "Conflict: New slot unavailable"}), 409

    data_store["appointments"][id].update(data)
    return jsonify({"message": "Rescheduled successfully"}), 200


# ROUND 4: Cancellation

@app.route('/v1/appointments/<int:id>', methods=['DELETE'])
def cancel_appointment(id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if id not in data_store["appointments"]:

        return jsonify({"error": "Appointment already cancelled or doesn't exist"}), 410

    del data_store["appointments"][id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=5001)