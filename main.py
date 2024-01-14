from functions import *
import csv

description_list = ["Subject", "Start Date", "Start Time","End Date", "End Time", "All Day Event", "Description", "Location", "Private"]
quarter = []

for weeks in range(0,70,7):
    for stuff in one_week(weeks):
        quarter.append(stuff)



#parse info into csv file
csv_file_path = 'Schedule.csv'

with open(csv_file_path, "w", newline='', encoding = 'utf-8') as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(quarter)
add_header_to_csv(csv_file_path, description_list)

