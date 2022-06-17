import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_links(url):
    baseurl='https://www.vivo.com'
    r=requests.get(url)
    sp=BeautifulSoup(r.text, 'lxml')
    links=sp.select('li.box-model-item a')
    return [baseurl + link.attrs['href'] for link in links]



def phone_data(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    data = {
        "Release_Date": sp.select_one('.no-flip-over:-soup-contains("Release date") + span').text,
        "Downloads": sp.select_one('.no-flip-over:-soup-contains("Downloads") + span').text,
    }
    return data


def main():
    urls=get_page_links('https://www.vivo.com/in/support/system-update')
    results=[phone_data(url) for url in urls]
    return results



df=pd.DataFrame(main())
df.to_csv("oppophones.csv", index=False)
print("Saved to CSV")














