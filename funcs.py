from re import search

import requests
from bs4 import BeautifulSoup

from vars import BASE, QUERY


class funcs:
    """Объект, содержащий в себе статические методы для парсинга.
    
    :staticmethod: get_html(url):
        Возвращает текстовое представление HTML-документа,
        расположенного по указанной ссылке.
    :staticmethod: get_total_pages(html):
        Возвращает общее количество страниц по текущему запросу
        в виде целого числа.
    :staticmethod: get_page_data(html):
        Получает распарсенные данные для каждой страницы
        и возвращает список релевантных запросов,
        организованных в формате кортежей.
    """
    @staticmethod
    def get_html(url):
        r = requests.get(url)
        return r.text


    @staticmethod
    def get_total_pages(html):
        soup = BeautifulSoup(html, 'lxml')
        pages = soup.find('div', class_='pagination-pages') \
                    .find_all('a', class_='pagination-page')
        last_page_url = pages[-1].get('href')
        total_pages = search(r'\d+', last_page_url).group()

        return int(total_pages) + 1

    
    @staticmethod
    def get_page_data(html):
        soup = BeautifulSoup(html, 'lxml')
        relevant_dataset = []
        ads = soup.find('div', class_='catalog-list') \
                  .find_all('div', class_='item_table')
        
        for ad in ads:
            header = ad.find('div', class_='item_table-header')
            title = header.find('h3', class_='item-description-title')
            title_text = title.span.get_text(strip=True)

            if QUERY[2:] not in title_text.lower():
                continue

            title_href = title.a['href']
            price = header.find('div', class_='about_bold-price') \
                          .find('span', class_='price')['content']

            data = (
                title_text,
                price,
                f'{BASE}' + title_href
            )

            relevant_dataset.append(data)

        return relevant_dataset
