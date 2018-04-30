# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()
import gevent
import time
import multiprocessing
import urllib2


def get_url(url):
    t1 = time.time()
    print("start", url)
    rsp = urllib2.urlopen(url)
    print("end using:%0.2f" % time.time() - t1, url, len(rsp.read()))


def child_process():
    t1 = time.time()
    gevent.joinall([
        gevent.spawn(get_url, "http://www.baidu.com"),
        gevent.spawn(get_url, "http://www.163.com")
    ])
    print("all using:%0.2f" % time.time() - t1)


def run():
    multiprocessing.Process(child_process)
    pass


if __name__ == "__main__":
    run()
    

