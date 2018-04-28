# coding: utf8
'''
Created on 2018年3月30日

@author: Administrator
'''
import sys
import time
import zmq


class ZmqClient(object):
    '''
    '''
    zmq_attr = {'request': zmq.REQ, 'subscribe': zmq.SUB, 'push': zmq.PUSH}

    def __init__(self, port, mode, push_port):
        self.mode = mode
        self.context = zmq.Context()
        self.socket = self.context.socket(ZmqClient.zmq_attr[mode])
        if 'push' == mode:
            self.socket.bind('tcp://*:{}'.format(push_port))
        else:
            self.socket.connect('tcp://localhost:{}'.format(port))
        
    def request(self):
        while True:
            data = raw_input('request input:')
            if 'q' == data:
                print('client exit.')
                return
            
            self.socket.send(data)
            
            rsp = self.socket.recv()
            print('rsp', rsp)
    
    def subscribe(self):
        self.socket.setsockopt(zmq.SUBSCRIBE, '')
        while True:
            data = self.socket.recv()
            print('subscribe recv', data)

    def push(self):
        while True:
            data = raw_input('push input:')
            if 'quit' == data:
                print('client quit.')
                sys.exit(0)
            self.socket.send(data)

    def run(self):
        call_mode = {'request': self.request, 'subscribe': self.subscribe, 'push': self.push}
        mode_func = call_mode[self.mode]
        print('client running in {} mode...'.format(self.mode))
        mode_func()
            

if __name__ == '__main__':
    if 2 != len(sys.argv):
        print('usage: request, subscribe, push')
        sys.exit()

    mode = sys.argv[1]

    client = ZmqClient(port = 1234, mode = mode, push_port = 1235)
    client.run()
