import time
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)


def csv_writer(platform, data):
    """
    Функция для записи данных в CSV
    """
    with open(f'{platform}.csv', "a", newline='', encoding='utf-8') as csv_file:
        '''
        csv_file - объект с данными
        delimiter - разделитель
        '''
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)


def search_customers(url):
    """
        Функция для нахождения всех поставщиков
    """
    browser.get(url)
    time.sleep(1)
    requiredhtml = browser.page_source
    soup = BeautifulSoup(requiredhtml, 'html5lib')
    respons = soup.find_all('div', {'class': 'search-registry-entry-block box-shadow-search-input'})
    numbers = []
    for respon in respons:
        numbers.append(respon.find('a').text.strip())
    for number in numbers:
        download("https://zakupki.gov.ru/epz/eruz/card/general-information.html?reestrNumber="+number[2:])


def download(href):
    """
            Парсинг информации о поставщике
    """
    
    print(href)


"""
cats = ['Город', 'Количество предложений', 'Количество онлайн предложений']
cities = ['Магадан', 'Екатеринбург', 'Волгоград', 'Сочи', 'Сургут', 'Краснодар']
urls_for_search = {'Магадан': 'https://realty.yandex.ru/magadan/kupit/kvartira/',
                   'Екатеринбург': 'https://realty.yandex.ru/ekaterinburg/kupit/kvartira/',
                   'Волгоград': 'https://realty.yandex.ru/volgograd/kupit/kvartira/',
                   'Сочи': 'https://realty.yandex.ru/sochi/kupit/kvartira/',
                   'Сургут': 'https://realty.yandex.ru/surgut/kupit/kvartira/ ',
                   'Краснодар': 'https://realty.yandex.ru/krasnodar/kupit/kvartira/'}
# hands = {'Магадан': ['49', '13'],
#          'Екатеринбург': ['11806', '82'],
#          'Волгоград': ['3850', '5'],
#          'Сочи': ['4661', '150'],
#          'Сургут': ['3050', '10'],
#          'Краснодар': ['21834', '17']}
csv_writer('data/flats', [cats])
for city in cities:
    number_of_offers = take_offers_info(urls_for_search.get(city))
    online_offers = take_online_info(urls_for_search.get(city))
    # data = [city, hands.get(city)[0], hands.get(city)[1]]
    data = [city, number_of_offers, online_offers]
    csv_writer('data/flats', [data])"""

ur = "https://zakupki.gov.ru/epz/eruz/search/results.html"
search_customers(ur)
browser.close()
