import eventlet as evl


def handler(conn, addreess):
    while True:
        data = conn.recv(1)
        if not data:
            print("connection is broken addr", address, conn)
            break
        conn.sendall(data)


def echo_server():
    srv = evl.listen(('0.0.0.0', 6000))
    print("starting listen 6000")
    pool = evl.GreenPool(10)

    while True:
        print("accept waiting for connecting ...")
        sock, addr = srv.accept()
        
        print("new client connected, addr is ", addr)
        pool.spawn_n(handler, sock, addr)


def run():
    echo_server()


if __name__ == "__main__":
    run()
