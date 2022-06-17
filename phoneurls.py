import requests
from bs4 import BeautifulSoup


url='https://www.oppo.com/in/smartphones/'

r=requests.get(url)
s=BeautifulSoup(r.text, 'html.parser')

phones=s.find_all('a', 'img-box')

for phone in phones:
    print(phone['href'])


