from bs4 import BeautifulSoup as bs

with open("schedule_yarwin.html") as fp:
    soup = bs(fp, 'html.parser')

#soup = bs("<html>a web page</html>", 'html.parser')

#print(bs("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))
# <html><head></head><body>Sacré bleu!</body></html>


#print(soup.prettify()) #prints out the html
print("title:", soup.title)
#print("class-item:", soup.class-item)
tag = soup.div
print("tag:", tag.attrs)


