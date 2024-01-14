def date_calculator(week_number):
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
    day = 8 + week_number * 7
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

print(date_calculator(9))

