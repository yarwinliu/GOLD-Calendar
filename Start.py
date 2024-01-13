from bs4 import BeautifulSoup as bs
import csv

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

#test if chunk of text is an element in the list -> each day and its classes are an element
#print(everyclass.pop(0))

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

    for elements in day_list:
        #removes day of week -> will replace with start day at [1][...]
        for day in DOW:
            if day in elements:
                day_list.remove(day)
        #

modified_array = [
    [subarray[i:i+3] for i in range(0, len(subarray), 3)]
    for subarray in classes_each_day
]

# Print the modified array
for subarray in modified_array:
    print(subarray)
    

#print(classes_each_day)

#parse info into csv file
csv_file_path = 'Schedule.csv'

with open(csv_file_path, "w", newline='', encoding = 'utf-8') as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(subarray)