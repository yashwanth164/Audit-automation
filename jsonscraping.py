import json
from openpyxl import Workbook

def extract_selected_parameters(json_data):
    extracted_parameters = []
    for doc in json_data['response']['response']['docs']:
        param_values = {
            'b_bid_number': doc.get('b_bid_number', [''])[0],
            'b_category_name': doc.get('b_category_name', [''])[0],
            'b_total_quantity': doc.get('b_total_quantity', [''])[0],
            'final_start_date_sort': doc.get('final_start_date_sort', [''])[0],
            'final_end_date_sort': doc.get('final_end_date_sort', [''])[0]
        }
        extracted_parameters.append(param_values)
    return extracted_parameters

def write_to_excel(data, sheet_name, wb):
    ws = wb.create_sheet(title=sheet_name)

    # Write headers
    headers = list(data[0].keys())
    ws.append(headers)

    # Write data
    for item in data:
        row_data = list(item.values())
        ws.append(row_data)

def main():
    wb = Workbook()

    # Iterate over the file names
    for i in range(1, 11):
        file_name = f'Page {i}.json'
        sheet_name = f'Sheet_{i}'

        # Read JSON data from file
        with open(file_name, 'r') as file:
            json_data = json.load(file)

        # Extract selected parameters
        extracted_data = extract_selected_parameters(json_data)

        # Write to Excel
        write_to_excel(extracted_data, sheet_name, wb)

    # Remove default sheet created by Workbook
    wb.remove(wb['Sheet'])

    # Save the workbook
    wb.save('output.xlsx')

if __name__ == "__main__":
    main()
