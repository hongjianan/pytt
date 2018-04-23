import eventlet as evl


def handler(conn, address):
    while True:
        data = conn.recv(1024)
        
        if not data:
            print("connection is broken addr", address, conn)
            break
        else:
            print("recv data:", data)
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
