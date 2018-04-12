# coding: UTF-8

from Queue import Queue


def queue_tt():
    queue = Queue(1)
    queue.put(1)
    queue.put(2)
    print(queue.get())
    print(queue.get())


def run():
    queue_tt()


if __name__ == "__main__":
    run()
