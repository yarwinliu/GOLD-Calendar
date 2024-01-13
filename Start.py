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

#test if chunk of text is an element in the list -> true
#print(everyclass.pop(0))

classnames = []

#adds class info (subject, location, start time to end time) to classnames list as text
for tag_element in everyclass:
   classnames.append(tag_element.text)
   classnames.strip()
   

print(classnames)