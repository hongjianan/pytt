# -*- coding: utf-8 -*-

import time
import socket


class TcpClient():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        self.tcp_client()

    def tcp_client(self):
        self.sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        print("connect to server port=%d success" % 54321)

        self.worker()

        self.sock.close()

    def worker(self):
        for idx in range(3):
            data = "hello" + str(idx)
            self.sock.sendall(bytes(data))
            print("send data: %s" % data)
            data = self.sock.recv(1024)
            print("server response:", str(data))


def run():
    for loop in range(1):
        client = TcpClient("127.0.0.1", 54321)
        client.run()
        time.sleep(1)


if __name__ == "__main__":
    run()
