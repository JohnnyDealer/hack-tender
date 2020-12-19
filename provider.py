import json
import requests
import regex as re
import pandas as pd
from bs4 import BeautifulSoup


def download_timetable():
    global error_counter
    req = requests.get('https://zakupki.gov.ru/epz/eruz/search/results.html')
    soup = BeautifulSoup(req.text, 'lxml')
    url = []
    for a in soup.find_all('a', class_='uk-link-toggle', href=True):
        if 'pdf' not in a['href'] and 'xlsx' in a['href'] or 'XLSX' in a['href']:
            url.append(a['href'])
            print(a['href'])

    for url_x in url:
        r = requests.get(url_x, allow_redirects=True)
        open(url_x.rsplit('/', 1)[1], 'wb').write(r.content)
        print(url_x.rsplit('/', 1)[1])

    print(error_counter)