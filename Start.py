from bs4 import BeautifulSoup as bs

print("hello world")
soup = bs("<html>a web page</html>", 'html.parser')
print(soup.prettify())