import eventlet

feedparser = eventlet.import_patched('feedparser')

def fetch_title(url):
    d = feedparser.parse(url)
    return d.feed.get('title', '')


def app(environ, start_rsp):
    pool = eventlet.GreenPool(100)
    pile = eventlet.GreenPile(pool)
    for url in environ['wsgi.input'].readlines():
        pile.spawn(fetch_title, url)
    titles = '\n'.join(pile)
    start_rsp()

