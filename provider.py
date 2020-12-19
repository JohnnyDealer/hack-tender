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


def search_customers(url, cust):
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
    buf_cust = {}
    for number in numbers:
        information = download("https://zakupki.gov.ru/epz/eruz/card/general-information.html?reestrNumber="+number[2:])
        for inf in information:
            buf_cust.update(inf)
        cust.update({number[2:]: buf_cust})


def download(href):
    """
            Парсинг информации о поставщике
    """
    browser.get(href)
    time.sleep(1)
    requiredhtml = browser.page_source
    soup = BeautifulSoup(requiredhtml, 'html5lib')
    contairs = soup.find('div', {'class': 'wrapper'}).find_all('div', {'class': 'container'})
    # Имя
    contair = contairs[3]
    blocks = contair.find_all('section', {'class': 'blockInfo__section section'})
    block = blocks[0]
    name = block.find('span', {'class': 'section__info'}).text
    # ИНН
    block = blocks[4]
    inn = block.find('span', {'class': 'section__info'}).text
    # КПП
    block = blocks[5]
    kpp = block.find('span', {'class': 'section__info'}).text
    # Контактное лицо
    contair = contairs[4]
    face = contair.find_all('td', {'class': 'tableBlock__col'})
    contair = contairs[5]
    blocks = contair.find_all('section', {'class': 'blockInfo__section section'})
    if len(blocks) == 1:
        # Телефон
        phone = 'None'
        # Email
        mail = mail = block.find('span', {'class': 'section__info'}).text
        # Адрес
        adress = 'None'
    else:
        # Телефон
        block = blocks[2]
        phone = block.find('span', {'class': 'section__info'}).text
        # Email
        block = blocks[1]
        mail = block.find('span', {'class': 'section__info'}).text
        # Адрес
        block = blocks[0]
        adress = block.find('span', {'class': 'section__info'}).text
    return [{'name': name}, {'adress': adress}, {'inn': inn}, {'kpp': kpp}, {'face': face}, {'phone': phone}, {'mail': mail}]


# Поставщики
customer = {}
ur = "https://zakupki.gov.ru/epz/eruz/search/results.html"
search_customers(ur, customer)
print(customer)
browser.close()
