import eventlet
from eventlet import wsgi


def hello_world(env, response):
    if env['PATH_INFO'] != '/':
        response('404 Not Found', [('Content-Type', 'text/plain')])
        return ['Not Found\r\n']

    response('200 OKK', [('Content-Type', 'text/plain')])
    return ['Hello World']


wsgi.server(eventlet.listen(('', 1000)), hello_world)
