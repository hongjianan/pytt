# coding: utf8
'''
Created on 2018年3月30日

@author: Administrator
'''
import sys
import time
import zmq

class ZmqServer(object):
    '''
    '''
    zmq_attr = {'reply': zmq.REP, 'publish': zmq.PUB, 'pull': zmq.PULL}

    def __init__(self, port, mode):
        self.port = port
        self.mode = mode
        self.context = zmq.Context()
        self.socket = self.context.socket(ZmqServer.zmq_attr[mode])
        self.socket.bind('tcp://*:{}'.format(port))
    
    def reply(self):
        while True:
            data = self.socket.recv()
            print('client requset', data)
            self.socket.send(data)
    
    def publish(self):
        while True:
            data = raw_input('input:')
            self.socket.send(data)

    def pull(self):
        while True:
            data = self.socket.recv()
            print('pull', data)
            
    def run(self):
        call_mode = {'reply': self.reply, 'publish': self.publish, 'pull': self.pull}
        mode_func = call_mode[self.mode]
        print('server running in {} mode...'.format(self.mode))
        mode_func()
      

if __name__ == '__main__':
    if 2 != len(sys.argv):
        print('usage: reply, publish, pull')
        sys.exit()

    mode = sys.argv[1]
    
    server = ZmqServer(1234, mode)
    server.run()
    