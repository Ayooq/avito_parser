from vars import *
from funcs import funcs
from csv_writer import csv_writerow


def main():
    first_page = f'{BASE}{REGION}{CATEGORY}?{QUERY}'
    html = funcs.get_html(first_page)
    total_pages = funcs.get_total_pages(html)
    
    data = ('Наименование объявления', 'Цена', 'Ссылка на страницу с товаром')
    csv_writerow('avito.csv', data)

    for num in range(1, total_pages):
        current_page = f'{BASE}{REGION}{CATEGORY}?{PAGE}{num}&{QUERY}'
        html = funcs.get_html(current_page)

        for elem in funcs.get_page_data(html):
                csv_writerow('avito.csv', elem, 'a')


if __name__ == '__main__':
    main()
