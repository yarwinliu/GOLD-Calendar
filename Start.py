from bs4 import BeautifulSoup as bs

with open("courtneys_schedule.html") as fp:
    soup = bs(fp, "html.parser")

#print(soup.prettify())

"""
parse subject, start date, start time and end time, location into csv file

- start date: calculated, looped 10 times
- create 10 google calendar events

"""

monday_classes = soup.find(id ="pageContent_eventsgroupM")

for c in soup.find_all('li'):
    if c != None:
        print(c.get('data-content'))


#print(monday_classes)
