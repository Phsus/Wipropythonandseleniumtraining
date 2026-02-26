from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask Server is Running!</h1>", 200


customers = {}
customer_counter = 1


@app.route('/customers', methods=['POST'])
def create_customer():
    global customer_counter
    data = request.json


    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing data"}), 400

    new_id = customer_counter
    customers[new_id] = {
        "id": new_id,
        "name": data['name'],
        "email": data['email'],
        "balance": data.get('balance', 0)
    }
    customer_counter += 1
    return jsonify(customers[new_id]), 201


@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = customers.get(id)
    if not customer:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(customer), 200


@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    if id not in customers:
        return jsonify({"error": "Not Found"}), 404

    data = request.json
    customers[id]['email'] = data.get('email', customers[id]['email'])
    return jsonify(customers[id]), 200


@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    if id in customers:
        del customers[id]
        return '', 204
    return jsonify({"error": "Not Found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)