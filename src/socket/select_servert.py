# -*- coding: utf-8 -*-

import socket
import select
import Queue


def worker(data):
    print("client request:", data)
    return bytes("ack:" + data)


def select_server_tt():
    input = []
    output = []
    msg_queues = {}
    timeout = 10

    server = socket.socket()
    server.bind(("127.0.0.1", 54321))
    server.listen(10)

    input.append(server)

    print("start server port=54321")

    while True:
        # print("---------- in server loop -----------")
        r_list, w_list, e_list = select.select(input, output, input, timeout)
        # error check
        for fd in e_list:
            print("fd error remove", fd)
            input.remove(fd)
            msg_queues.pop(fd)

        # data check
        for fd in r_list:
            if fd == server:
                client, address = server.accept()
                print("client connected", address)
                input.append(client)
                msg_queues[client] = Queue.Queue()
            else:
                try:
                    data = fd.recv(1024)
                    if data:
                        data = str(data)
                        response = worker(data)
                        msg_queues[fd].put(response)    # 将响应写入发送队列

                        if fd not in output:
                            output.append(fd)
                    else:   # client close socket
                        input.remove(fd)
                        msg_queues.pop(fd)
                        print("client close:", fd)
                except Exception as e:
                    input.remove(fd)
                    msg_queues.pop(fd)
                    print("client fd", fd, e)

        # write check
        for fd in w_list:
            if fd in msg_queues:
                queue = msg_queues[fd]
                while not queue.empty():
                    data = queue.get(False)
                    fd.sendall(data)
                    print("fd write", fd)


def select_multi_server_tt():
    servers = []
    for port in range(54321, 54323):
        server = socket.socket()
        server.bind(("127.0.0.1", port))
        server.listen(10)
        servers.append(server)

    while True:
        r_list, w_list, e_list = select.select(servers, servers, servers, 1)
        for server in r_list:
            client, address = server.accept()
            print("client connected", server, address)

        for server in w_list:
            client, address = server.accept()
            print("client connected", server, address)


def run():
    # select_multi_server_tt()
    select_server_tt()


if __name__ == "__main__":
    run()
