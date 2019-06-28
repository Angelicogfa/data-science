import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen('https://www.python.org') as url:
    page = url.read()

print(page)

soup = BeautifulSoup(page, 'html.parser')
soup
soup.title
soup.title.text

soup.find_all('a')
tables = soup.find('table')
tables
print(tables)


