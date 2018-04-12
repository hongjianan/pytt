# coding: UTF-8

from gevent import monkey
monkey.patch_all()   # 修改阻塞io
import gevent
import urllib2
import time


def get_url(url, flag):
    t1 = time.time()
    print("start", url)
    rsp = urllib2.urlopen(url)
    print("end", url, len(rsp.read()))
    print(time.time() - t1)

    if flag:
        gevent.sleep(1)
        print("sleep ======")
    else:
        print("======")

    time.sleep(3)


def gevent_tt():
    t1 = time.time()
    gevent.joinall([
        gevent.spawn(get_url, "http://www.163.com", False),
        gevent.spawn(get_url, "http://www.baidu.com", False),
        gevent.spawn(get_url, "http://www.qq.com", False),
        gevent.spawn(get_url, "http://www.taobao.com", True),
    ])

    print("all", time.time() - t1)


def run():
    gevent_tt()


if __name__ == "__main__":
    run()
    

