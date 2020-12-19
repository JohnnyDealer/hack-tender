from bs4 import BeautifulSoup
from pip._vendor import requests
import json


def parser_go_br():
    req = requests.get("https://zakupki.gov.ru/epz/orderplan/search/results.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&structured=true&fz44=on&customerPlaceWithNested=on&actualPeriodRangeYearFrom=2020&sortBy=BY_MODIFY_DATE&pageNumber=1&sortDirection=false&recordsPerPage=_10&searchType=false%22")
    soup = BeautifulSoup(req.text, 'lxml')
    links = soup.find_all(class_='registry-entry__header-mid__number')
    jsonfile = {'list': []}
    for i in links:
        content_list = []
        a = i.find('a')
        req2 = requests.get('https://zakupki.gov.ru/' + a['href'])
        soup2 = BeautifulSoup(req2.text, 'lxml')
        sections = soup2.find_all('section')
        for j in sections:
            content = j.find(class_='section__info')
            if content is not None:
                content_list.append(content.text.strip())
        jsonfile['list'].append({'unique': content_list[0], 'planning_year': content_list[1], 'period': content_list[2],
                             'confirm_date': content_list[3], 'FIO': content_list[4], 'place_date': content_list[5],
                             'status': content_list[6], 'customer': content_list[7], 'INN': content_list[8],
                             'OKOPF': content_list[9], 'form': content_list[10], 'OKTMO': content_list[11],
                             'education': content_list[12], 'address': content_list[13], 'phone': content_list[14],
                             'email': content_list[15]})
    if not (jsonfile == {} or jsonfile == ''):
        with open('plan' + '.json', 'w', encoding='utf-8') as write_file:
            json.dump(jsonfile, write_file, indent=4, ensure_ascii=False)


parser_go_br()