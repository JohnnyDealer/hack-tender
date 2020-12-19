from bs4 import BeautifulSoup
from pip._vendor import requests
import json


def plan():
    req = requests.get("https://zakupki.gov.ru/epz/orderplan/search/results.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&structured=true&fz44=on&customerPlaceWithNested=on&actualPeriodRangeYearFrom=2020&sortBy=BY_MODIFY_DATE&pageNumber=1&sortDirection=false&recordsPerPage=_10&searchType=false%22")
    soup = BeautifulSoup(req.text, 'lxml')
    burls = []
    for a in soup.find_all('a', href=True):
        if 'plan-number' in a['href'] and 'journal-events' not in a['href']:
            burls.append(a.text.strip())
    urls = []
    for b in burls:
        if '№' in b:
            urls.append('https://zakupki.gov.ru/epz/orderplan/pg2020/general-info.html?plan-number=' + b[2:])
    print(urls)
    content_title_list = []
    content_info_list = []
    jsonfile = {'list': []}
    for num, url_x in enumerate(urls, 0):
        print(num)
        print(url_x)
        provider_data = requests.get(url_x, allow_redirects=True)
        soup2 = BeautifulSoup(provider_data.text, 'lxml')
        containers = soup2.find_all("section")
        for j in containers:
            content_title = j.find(class_='section__title')
            content_info = j.find(class_='section__info')
            if (content_title and content_info) is not None:
                content_title_list.append(content_title.text.strip())
                content_info_list.append(content_info.text.strip())
        json1block = {}
        for i in range(len(content_info_list)):
            json1block[content_title_list[i]] = content_info_list[i]
        jsonfile['list'].append(json1block)
        if not (jsonfile == {} or jsonfile == ''):
            with open('purchase_plan' + '.json', 'w', encoding='utf-8') as write_file:
                json.dump(jsonfile, write_file, indent=4, ensure_ascii=False)
        print('---------------------------------------------------------------')


plan()
