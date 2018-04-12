# coding: UTF-8

import random
import urllib
import urllib2
import cookielib


ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]


def cookie_test():
    cookie = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)

    opener = urllib2.build_opener(cookie_handler)
    opener.addheaders = [("User-agent" , random.choice(ua_list))]

    url = "https://mail.163.com/?msg=authfail#return"

    acount = {"email" : "hjnhong@163.com", "password" : "059123396005hong"}
    acount = urllib.urlencode(acount)

    req = urllib2.Request(url, data = acount)
    rsp = opener.open(req)
    print(rsp.getcode())
    print(rsp.read())


def run():
    cookie_test()


if __name__ == "__main__":
    run()
