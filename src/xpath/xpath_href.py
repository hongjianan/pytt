# coding:utf-8

import sys
import urllib
import urllib2
import requests
from lxml import etree

index_url = "http://www.xfzy07.com/html/an"


def get_ref(url):
    rsp = requests.get(url = url)
    if 200 != rsp.status_code:
        print("response is fail, code=%s" % rsp.status_code)
        return -1
    html = rsp.text

    content = etree.HTML(html)
    # refs = content.xpath('//div[@class="wrap"]/div[@id="wrap"]/div[@id="ks"]/div[@id=ks_xp]//div[@class="list"]//ul//a/@href')
    refs = content.xpath('//ul//td[@width="888"]/a/@href')
    # refs = content.xpath('//ul//a/@href')
    print(type(refs))
    return refs


def run():

    start_page = 1
    end_page = 1
    while start_page <= end_page:
        if 1 == start_page:
            url = index_url
        else:
            url = index_url + "index" + str(start_page) + ".html"
        print(url)
        refs = get_ref(url)
        for ref in refs:
            url = index_url + ref
            print(url)
            ttt = get_ref(url)
            print(ttt)

        start_page += 1


if __name__ == "__main__":
    run()
