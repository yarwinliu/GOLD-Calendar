from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime

with open("megan_schedule.html") as fp:
    soup = bs(fp, "html.parser")

def format_date(x):
    """
    returns list depending on param
    """
    month_dic = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    month = 1
    day = 8 + x
    year = 24

    if day >= month_dic[month]:
        month += 1
        p = month
        while p > 0:
            day = day - month_dic[p]
            p-=1

    if day <= 10:
        sday = "0"+ str(day)
    else:
        sday = str(day)
    if month <= 10:
        smonth = "0"+ str(month)
    else:
        smonth = str(month)

    if month >12:
        year += 1
        syear = str(year)
    else:
        syear = str(year)

    date = smonth + "/" + sday + "/" + syear

    return date


def standard_to_military(time_str):
    dt_object = datetime.strptime(time_str, "%I:%M %p")
    military_time = dt_object.strftime("%H:%M")

    return military_time

def one_week(days):

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
    print(classes_each_day)

    for idx, day_list in enumerate(classes_each_day):
        start_date = format_date(idx)        
        # removes empty objects
        while "" in day_list:
            day_list.remove("")   

        for index, elements in enumerate(day_list):
            # if ":" in elements:
            #     day_list.insert(index-1,start_date)


            # x = len(day_list)/4
            # p=1
            # a=0
            # while p<=x:
            #     a+=2
            #     day_list.insert(a,start_date)
            #     day_list.insert(a+2,start_date)
            #     a+=4
            #     p+=1


            removes day of week -> will replace with start day at [1][...]
            for day in DOW:
                if day in elements:
                    day_list.remove(day)

            #converts standard time to military time
            if "AM" in elements or "PM" in elements:
                day_list[index] = standard_to_military(elements)
            #split times into start/end times
            for i in range(len(day_list)):
                day_list[i:i+1] = day_list[i].split('-')

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

    return flat_list

print(one_week(1))