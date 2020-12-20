import json
import requests
from bs4 import BeautifulSoup
from database.app.uof import ProviderBuilder

def parse_provider_links():
    req = requests.get('https://zakupki.gov.ru/epz/contract/search/results.html')
    soup = BeautifulSoup(req.text, 'lxml')
    url = []
    for a in soup.find_all('a', href=True):
        if 'reestrNumber' in a['href'] and 'journal-events' not in a['href'] and a['href'] not in url:
            url.append(a['href'])
    url_starter = 'https://zakupki.gov.ru/epz/contract/contractCard/common-info.html?reestrNumber='
    content_title_list = []
    content_info_list = []
    jsonfile = {'list': []}
    for num, url_x in enumerate(url, 0):
        provider_data = requests.get(url_starter+url_x, allow_redirects=True)
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
            with open('provider' + '.json', 'w', encoding='utf-8') as write_file:
                json.dump(jsonfile, write_file, indent=4, ensure_ascii=False)
        print('---------------------------------------------------------------')
    ProviderBuilder.build(dictionary_list=jsonfile['list'])


""" Пример использования """


parse_provider_links()
