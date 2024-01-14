from functions import *
description_list = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]


#parse info into csv file
csv_file_path = 'Schedule.csv'

def add_header_to_csv(file_path, header_list):
    # Read existing content from the CSV file
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        existing_data = list(reader)

    # Insert the new header at the beginning
    existing_data.insert(0, header_list)

    # Write the updated content back to the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(existing_data)


add_header_to_csv(csv_file_path, description_list)

# with open(csv_file_path, "w", newline='', encoding = 'utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(one_week())