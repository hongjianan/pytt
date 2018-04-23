import eventlet
from eventlet.green import socket

class BroadcastClient():
    def __init__(self, pool, srv_port, num):
        self.pool = pool
        self.srv_port = srv_port
        self.num = num

    def multi_send(self):
        pile = eventlet.GreenPile(self.pool)
        for times in range(self.num):
            print("spawn times=%d" % times)
            pile.spawn(self.send_msg, times)

    def send_msg(self, times):
        print("send msg times", times)
        try:
            sock = socket.socket()
            sock.connect(("127.0.0.1", self.srv_port))
            sock.sendall("times " + str(times))
            
            sock.recv(1024)
            sock.close()
        except ex:
            print(ex)


def run():
    pool = eventlet.GreenPool()
    client = BroadcastClient(pool, 6000, 3)
    client.multi_send()

    eventlet.sleep(10)



if __name__ == '__main__':
    run()