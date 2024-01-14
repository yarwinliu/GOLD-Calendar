from functions import *



#parse info into csv file
csv_file_path = 'Schedule.csv'

with open(csv_file_path, "w", newline='', encoding = 'utf-8') as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(one_week())