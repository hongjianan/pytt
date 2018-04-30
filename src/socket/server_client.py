# -*- coding: utf-8 -*-

import time
import socket
import threading


class TcpServer(threading.Thread):
    def __init__(self):
        super(TcpServer, self).__init__()

    def run(self):
        self.tcp_server()

    def tcp_server(self):
        sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 54321))
        sock.listen(10)
        while True:
            client, address = sock.accept()
            print(address, "connected")
            data = client.recv(1024)
            print("receive data:", data)

        sock.close()


class TcpClient(threading.Thread):
    def __init__(self):
        super(TcpClient, self).__init__()

    def run(self):
        self.tcp_client()

    def tcp_client(self):
        sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 54321))
        sock.sendall("hello")
        sock.close()


def run():
    print(dir(socket.socket()))

    server_thread = TcpServer()
    client_thread = TcpClient()

    thread_pool = []
    thread_pool.append(server_thread)
    thread_pool.append(client_thread)

    server_thread.start()

    time.sleep(1)
    client_thread.start()

    for t in thread_pool:
        t.join()


if __name__ == "__main__":
    run()
