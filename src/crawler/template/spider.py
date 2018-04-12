# coding:UTF-8

import sys
from imp import reload
import string
import chardet
import urllib
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("UTF-8")

HOST = "http://www.xfzy07.com"
URL = "http://www.xfzy07.com/html/an/"
# URL = "http://www.xfzy07.com/html/an/104117/"
START_PAGE = 33494
END_PAGE = 127565


def get_soup(page_url):
    rsp = requests.get(url = page_url)
    # print(type(rsp.status_code), rsp.status_code)
    # print(rsp.encoding)
    if 200 != rsp.status_code:
        print("response is fail, code=%s" % rsp.status_code)
        return -1

    return BeautifulSoup(rsp.text, "lxml")


def get_audio(page_url):
    soup = get_soup(page_url)
    if -1 == soup:
        return -1

    audios = soup.select("audio")

    for audio in audios:
        audio_url = audio.get("src").decode("utf-8").encode("ISO-8859-1").decode("gbk").encode("utf-8")
        print(audio_url)
        return audio_url

    return -1

'''
def get_href(page_url):
    soup = get_soup(page_url)
    if -1 == soup:
        return -1
    refs = soup.select("body > div.wrap > div.ks > div.ks_xp > div.main > div.list > ul")
    print(refs)
'''


def spider(start_page, end_page):

    try_times = 1
    while start_page <= end_page:
        try:
            full_url = URL + str(start_page)
            audio = get_audio(full_url)
            if -1 != audio:
                print("==OK ## %s ## %s" % (full_url, audio))
        except Exception as e:
            print(try_times, e.message)
            try_times += 1
            if try_times <= 3:
                continue
            break

        try_times = 1
        start_page += 1


def write2file(filename, records):
    with open(filename, "wr") as f:
        for record in records:
            f.write(record)


def run():
    spider(START_PAGE, END_PAGE)

if __name__ == "__main__":
    run()
