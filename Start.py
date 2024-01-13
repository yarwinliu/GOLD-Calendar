from bs4 import BeautifulSoup

with open("courtneys_schedule.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

print(soup.prettify())
