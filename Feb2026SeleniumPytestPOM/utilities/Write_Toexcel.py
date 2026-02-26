import openpyxl


def get_excel_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []


    for row in sheet.iter_rows(min_row=1, values_only=True):
        username = row[0]
        password = row[1]


        if username is not None and "Username" not in str(username):
            data.append((username, password))

    return data