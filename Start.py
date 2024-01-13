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

# all instances of li in classes 'section'
every_class = classes.find_next_siblings('li')
every_class.insert(0, classes.find_next('li'))

# monday: classes.find_next('li')
# tuesday-friday: classes.find_next_siblings('li')

#prints out subject, location, start time to end time
for info in every_class:
    print(info.text)
