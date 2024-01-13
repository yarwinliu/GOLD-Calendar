from bs4 import BeautifulSoup as bs

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

mon = mondayclasses.find_next('li')
tues2fri = classes.find_next_siblings('li')

everyclass = tues2fri
everyclass.insert(0, mon)

#test if chunk of text is an element in the list -> each day and its classes are an element
#print(everyclass.pop(0))

classes_each_day = []

#adds class info (subject, location, start time to end time) to classnames list as strings
for tag_element in everyclass:
   p = tag_element.text
   x = p.split("\n")
   classes_each_day.append(x)

# classes_each_day is a 2d array
# removes empty objects
element_to_remove = ""
for day in classes_each_day:
    while element_to_remove in day:
        day.remove(element_to_remove)


print(classes_each_day)
