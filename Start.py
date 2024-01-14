from bs4 import BeautifulSoup as bs
import csv
from functions import *

with open("courtneys_schedule.html") as fp:
    soup = bs(fp, "html.parser")

#print(soup.prettify())

"""
parse subject, start date, start time and end time, location into csv file

- start date: calculated, looped 10 times
- create 10 google calendar events

"""

#classes 'section' of html file
classes = soup.find(id = 'pageContent_eventsgroupM')
mondayclasses = soup.find(id = 'pageContent_events')

# all instances of li in classes 'section'

mon_html = mondayclasses.find_next('li')
tues2fri_html = classes.find_next_siblings('li')

everyclass = tues2fri_html
everyclass.insert(0, mon_html)

#each day and its classes are an element

classes_each_day = []
DOW = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

#adds class info (subject, location, start time to end time) to classnames list as strings
for tag_element in everyclass:
   text_element = tag_element.text
   empty_text_element = text_element.split("\n") # empty meaning not white space
   classes_each_day.append(empty_text_element)

# classes_each_day is a 2d array

element_to_remove = ""
for day_list in classes_each_day:
    # removes empty objects
    while element_to_remove in day_list:
        day_list.remove(element_to_remove)

    for index, elements in enumerate(day_list):
        #removes day of week -> will replace with start day at [1][...]
        for day in DOW:
            if day in elements:
                day_list.remove(day)
        #converts standard time to military time
        if "AM" in elements or "PM" in elements:
            day_list[index] = standard_to_military(elements)
        #split times into start/end times
        for i in range(len(day_list)):
            day_list[i:i+1] = day_list[i].split('-')


print(classes_each_day)
# in classes_each_day array, separate each class and its info into its own subarray
modified_array = [
    #change to 8s once all elements r in !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    [subarray[i:i+4] for i in range(0, len(subarray), 4)]
    for subarray in classes_each_day
]
#flatten 3d array to 2d array to display on separate rows for csv file   
flat_list = [elem for sublist1 in modified_array for elem in sublist1]

#rearrange each subarray for csv formatting
for subarray in flat_list:
      #fix once start/end times/dates are added
    location = subarray.pop(1)
    all_day_event = subarray.append(False)
    description = subarray.append("Description")
    subarray.append(location)
    private = subarray.append(False)

#parse info into csv file
csv_file_path = 'Schedule.csv'

with open(csv_file_path, "w", newline='', encoding = 'utf-8') as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(flat_list)