""" 
parse into csv file: has header, put info below header
need:
 subject,
 start date(hard coded for now, calculating) +7, 
 start time, 
 end time, 
 location,


2 variables: all monday class (list), monday time

week = [monday, tuesday, wednesday, thursday, friday]

for day in week,
    function-- class_grabber(day(string)): data-content
        returns class names (list) 

no function for start date

for loop: for x in class_names,
    function-- start_time(day(string), x): data-start
        returns start time (string)

    function-- end_time(day(string), x): data-end
        returns end time (string)

    function-- location(x): data-event
    returns location (string)
 """
import csv
from bs4 import BeautifulSoup as bs

with open("megan_schedule.html") as fp:
    soup = bs(fp, "html.parser")

# # ------------------------------------------------------------------------------
    
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
   empty_text_element = text_element.split("\n") #empty meaning not white space
   classes_each_day.append(empty_text_element)

# classes_each_day is a 2d array
# removes empty objects
element_to_remove = ""
for day_list in classes_each_day:
    #removes empty objects from list
    while element_to_remove in day_list:
        day_list.remove(element_to_remove)
    #gets rid of mon-fri
    for elements in day_list:
        for day in DOW:
            if day in elements:
                day_list.remove(day)

# in classes_each_day array, separate each class and its info into its own subarray
modified_array = [
    [subarray[i:i+3] for i in range(0, len(subarray), 3)]
    for subarray in classes_each_day
]
# print the modified array
# for subarray in modified_array:
#     print(subarray)

#flatten 3d array to 2d array to display on separate rows for csv file   
flat_list = [elem for sublist1 in modified_array for elem in sublist1]

print(classes_each_day)


# csv_file_path = 'Schedule.csv'

# with open(csv_file_path, "w", newline='', encoding = 'utf-8') as csv_file:

#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(modified_array)

