# !pip install tabulate
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = 'http://www.nationmaster.com/country-info/stats/Media/Internet-users'

res = requests.get(url)

soup = BeautifulSoup(res.content, 'lxml')

table = soup.find_all('table')[0]

df = pd.read_html(str(table))

print(df)

print(df[0].to_json(orient='records'))

res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')
df = pd.read_html(str(soup.table))
print(tabulate(df[0], headers = 'keys', tablefmt = 'psql'))