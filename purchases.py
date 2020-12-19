import json
import requests
from bs4 import BeautifulSoup


def parse_purchase_short(urls):
    return 1


def parse_purchase_long(urls):
    content_title_list = []
    content_info_list = []
    jsonfile = {'list': []}
    for num, url_x in enumerate(urls, 0):
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
            with open('purchases' + '.json', 'w', encoding='utf-8') as write_file:
                json.dump(jsonfile, write_file, indent=4, ensure_ascii=False)
        print('---------------------------------------------------------------')


def parse_purchase_links():
    req = requests.get('https://zakupki.gov.ru/epz/order/extendedsearch/results.html')
    soup = BeautifulSoup(req.text, 'lxml')
    burls = []
    for a in soup.find_all('a', href=True):
        if 'regNumber' in a['href'] and 'journal-events' not in a['href'] and a.text not in burls:
            burls.append(a.text.strip())
    url_starter_short = 'https://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber='
    url_starter_long = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber='
    for url in burls:
        if '№' in url:
            if len(url[2:]) < 12:
                urlS.append(url_starter_short + url[2:])
            else:
                urlL.append(url_starter_long + url[2:])
                print(url_starter_long + url[2:])


urlS = []
urlL = []
parse_purchase_links()
parse_purchase_long(urlL)
