from bs4 import BeautifulSoup as bs

with open("courtneys_schedule.html") as fp:
    soup = bs(fp, "html.parser")

#print(soup.prettify())

"""
parse subject, start date, start time and end time, location into csv file

- start date: calculated, looped 10 times
- create 10 google calendar events

"""

#monday 'section' of html file
monday_classes = soup.find(id = 'pageContent_eventsgroupM')

"""
iterates through entire html file to find class names 
-> we are trying to iterate through only the monday section
"""
#for c in soup.find_all('li'):

    #print(c.get('data-content'))


next_paragraphs = monday_classes.find_next('li')

for paragraph in next_paragraphs:
    print(paragraph.text)
