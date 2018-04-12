import eventlet
from eventlet.green import urllib

urls = [
    "https://www.google.com/intl/en_ALL/images/logo.gif",
    "http://python.org/images/python-logo.gif",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]


def fetch(url):
    print("open url %s" % url)
    body = urllib.urlopen(url).read()
    print("done url %s" % url)
    return url, body


def multi_rul():
    pool = eventlet.GreenPool(100)
    for url, body in pool.imap(fetch, urls):
        print("from url:%s", url, "length:", len(body))


def run():
    multi_rul()


if __name__ == "__main__":
    run()
