# coding: UTF-8

import threading
import time

EVENT = threading.Event()


def thread_wait(event):
    for i in range(5):
        event.wait(timeout = 2)
        print("wait flag=%s" % event.isSet())
        event.clear()


def thread_set(event):
    for i in range(5):
        event.set()
        print("set flag=%s" % event.isSet())
        time.sleep(1)


def run():
    threads = []
    threads.append(threading.Thread(target = thread_wait, args=(EVENT,)))
    threads.append(threading.Thread(target = thread_wait, args = (EVENT,)))
    threads.append(threading.Thread(target = thread_set, args=(EVENT,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    run()
    

