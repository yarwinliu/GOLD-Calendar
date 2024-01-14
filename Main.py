from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime

with open("megan_schedule.html") as fp:
    soup = bs(fp, "html.parser")
"""
parse subject, start date, start time and end time, location into csv file

- start date: calculated, looped 10 times
- create 10 google calendar events

"""
subject = []
startDate = []
startTime = []
endTime = []
loc =[]
bigarray = []

for tag in soup.find_all('h1', class_="event-name"):
    title = tag.text
    subject.append(title)

for tag in soup.find_all('h2', class_="event-location"):
    title = tag.text
    loc.append(title)

classes = soup.find(id = 'pageContent_eventsgroupM')
mondayclasses = soup.find(id = 'pageContent_events')

mon_html = mondayclasses.find_next('li')
tues2fri_html = classes.find_next_siblings('li')

everyclass = tues2fri_html
everyclass.insert(0, mon_html)

print(everyclass) #everyclass is bigger lists

print("--------------------")
print(everyclass.find_all_next('li'))
#for element in everyclass:
    


#print(soup.find_all('li', class_="single-event"))
# for tag in soup.find_all('h1', class_="event-name"):
#     title = tag.text
#     subject.append(title)

# for tag in soup.find_all('h1', class_="event-name"):
#     title = tag.text
#     subject.append(title)

print(loc)

#parse info into csv file
# csv_file_path = 'schedule.csv'

# with open(csv_file_path, "w", newline='', encoding = 'utf-8') as csv_file:

#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(one_week())