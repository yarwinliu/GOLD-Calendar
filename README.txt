INSTRUCTIONS FOR USE

Prerequisites:
- Windows computer
- Python
- beautiful soup (html parser): https://www.geeksforgeeks.org/beautifulsoup-installation-python/

0. To start fresh (removed cached files)
    a. delete token files/toekn_calendar_v3.pickle
    b. delete excel_files.xlsx and csv_file.csv
1. Get the html for your schedule
    a. log into GOLD 
    b. click MY SCHEDULE on the top bar
    c. Schedule Weekly View in the upper right corner
    d. right click > View page source
    e. copy the whole html file
    f. paste into the file called schedule.html of GOLD-Calendar 
2. run main.py (puts tgt the html to csv and csv to calendar)

ISSUES
- in html to csv, the end date col is missing

TESTING
- TESTcsv_file.csv and TESTexcel_file.xlsx demonstrate expected behavior (for csv_file.csv and excel_file.xlsx) when main.py is run
- megan_schedule.html and megan_schedule.csv are also expected behavior (for html to csv)
