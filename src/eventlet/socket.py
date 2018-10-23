from __future__ import print_function

import eventlet
# from eventlet.green import socket


def geturl(url):
    sock = socket.socket()
    ip = socket.gethostbyname(url)
    sock.connect((ip, 80))
    print('%s connected' % url)
    sock.sendall('''GET \r\n\r\n''')
    return sock.recv(100)


def geturls():
    urls = ['www.google.com', 'www.yandex.ru', 'www.python.org']
    pile = eventlet.GreenPile()
    for url in urls:
        pile.spawn(geturl, url)

    for url, rsp in zip(urls, pile):
        print('%s: %s' % (url, rsp))
