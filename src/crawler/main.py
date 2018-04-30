# -*- coding: utf-8 -*-

try: #python2
    from urlparse import urljoin
except ImportError: #python3
    from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests
import csv
import html5lib

OUT_FMT = 'gbk'
URL  = 'http://bj.ganji.com/fang1/o%7Bpage%7Dp%7Bprice%7D/'
ADDR = 'http://bj.ganji.com'

LIST_FMT = '.f-list > .f-list-item > .f-list-item-wrap'


if __name__ == '__main__':
    start_page = 1
    end_page = 10
    price = 7

    with open('ganji.csv', 'wb') as f:
        csv_writer = csv.writer(f, delimiter = ',')
        print('start ......')

        while start_page <= end_page:
            start_page += 1
            print('get:{0}'.format(URL.format(page = start_page, price = price)))
            response = requests.get(URL.format(page = start_page, price = price))

            html = BeautifulSoup(response.text, 'html.parser')
            house_list = html.select(LIST_FMT)

            if not house_list:
                break

            for house in house_list:
                house_title = house.select('.title > a')[0].string.encode(OUT_FMT)
                house_addr  = house.select('.address > .area > a')[-1].string.encode(OUT_FMT)
                # house_price = house.select('.info > .price > num')[0].string.encode(OUT_FMT)
                house_url   = urljoin(ADDR, house.select('.title > a')[0]['href'])

                # csv_writer.writerow([house_title, house_addr, house_price, house_url])
                csv_writer.writerow([house_title, house_addr, house_url])

        print('end  ......')

