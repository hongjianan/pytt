# coding: UTF-8

import sys
import zmq


class ZmqWorker(object):
    '''
    '''

    def __init__(self, pull_port, push_port):
        self.context = zmq.Context()
        self.pull = self.context.socket(zmq.PULL)
        self.pull.connect('tcp://localhost:{}'.format(pull_port))

        self.push = self.context.socket(zmq.PUSH)
        self.push.connect('tcp://localhost:{}'.format(push_port))

    def pull_push(self):
        while True:
            data = self.pull.recv()
            print('pull recv', data)
            self.push.send(data)

    def run(self):
        self.pull_push()


if __name__ == '__main__':
    worker = ZmqWorker(1235, 1234)
    worker.run()
