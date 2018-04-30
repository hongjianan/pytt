# -*- coding: utf-8 -*-

import random
import urllib
import urllib2
import ssl


URL_12306 = "https://www.12306.cn/mormhweb/"
IGNORE_AC = True
PROXY_SWITCH = False

ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]


def opener_test():
    http = urllib2.HTTPHandler(debuglevel = 1)
    opener = urllib2.build_opener(http)

    req = urllib2.Request("http://www.baidu.com/", headers = {"User-Agent": random.choice(ua_list)})
    rsp = opener.open(req)
    print(rsp.read())


def proxy_test():
    if PROXY_SWITCH:
        proxy = urllib2.ProxyHandler({"http": "127.0.0.1:8888"})
    else:
        proxy = urllib2.ProxyHandler({})

    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    rsp = agent_req("http://www.baidu.com/")
    print(rsp.read())


def ssl_test():
    # 忽略SSL安全认证
    req = urllib2.Request(URL_12306, headers = {"User-Agent": random.choice(ua_list)})
    if IGNORE_AC:
        print("not ignore ac")
        rsp = urllib2.urlopen(req, context = ssl._create_unverified_context())
    else:
        print("ignore ac")
        rsp = urllib2.urlopen(req)
    print(rsp.read())


def post_test():
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",

        "User-Agent": random.choice(ua_list),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    word = raw_input("please input word need translate:")
    print("your input is %s" % word)

    form_data = {
        "type": "AUTO",
        "i": word,
        "doctype": "json",
        "xmlVersion": "1.8",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    data = urllib.urlencode(form_data)

    req = urllib2.Request(url, data = data, headers = headers)
    rsp = urllib2.urlopen(url = req, timeout = 1000)
    js = rsp.read()
    print(js)



def request_test():

    headers = {
        "User-agent" : random.choice(ua_list)
    }

    req = urllib2.Request("http://www.baidu.com/", headers = headers)
    rsp = urllib2.urlopen(req)
    html = rsp.read()

    print(type(rsp), dir(rsp))
    print(type(html), len(html))


def urlopen_test():
    rsp = urllib2.urlopen("http://www.baidu.com/")
    print(type(rsp), dir(rsp))
    html = rsp.read()

    print("len", len(html))
    print("getcode", rsp.getcode())
    print("geturl", rsp.geturl())
    print("info", type(rsp.info()), dir(rsp.info()), rsp.info())
    print("fileno", rsp.fileno)
    print("code", rsp.code)

    header = rsp.info()

    print(len(header))
    print("getdate %s" % header.getdate)
    print(header.getdate)


def agent_req(url):
    req = urllib2.Request(url, headers = {"User-Agent": random.choice(ua_list)})
    return urllib2.urlopen(req)


def run():
    # urlopen_test()
    # request_test()
    # post_test()
    # ssl_test()
    # proxy_test()
    opener_test()


if __name__ == "__main__":
    run()
