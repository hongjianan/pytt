# coding: UTF-8

import time
import threading
import pika


def rabbitmq_producer():
    print("tid[%s] producer start ..." % threading.currentThread())
    connect = pika.BlockingConnection(pika.ConnectionParameters(host = "192.168.1.131"))
    channel = connect.channel()
    channel.queue_declare(queue = "time_message", durable = False) # 持久化参数

    for i in range(2):
        stime = str(time.time())
        # stime = str(i)
        channel.basic_publish(exchange = "",
                              routing_key = "time_message",
                              body = stime)
        print("--> send message: %s" % stime)
        time.sleep(1)

    connect.close()
    print("======== producer end ==========")


def rabbitmq_consumer():
    print("tid[%s] consumer start ..." % threading.currentThread())
    connect = pika.BlockingConnection(pika.ConnectionParameters(host = "192.168.1.131"))
    channel = connect.channel()
    channel.queue_declare(queue = "time_message")

    def callback(ch, method, properties, body):
        print("tid[%s] <-- recv message: %r" % (threading.currentThread(), body))
        # time.sleep(2)
        print("callback end")

    channel.basic_consume(callback,
                          queue = "time_message",
                          no_ack = True)

    channel.start_consuming()
    print("======== consumer end ==========")


def rabbitmq_tt():
    ts = []
    ts.append(threading.Thread(target = rabbitmq_producer))
    ts.append(threading.Thread(target = rabbitmq_consumer))
    ts.append(threading.Thread(target = rabbitmq_consumer))

    for t in ts:
        t.start()

    for t in ts:
        t.join()


def run():
    rabbitmq_tt()


if __name__ == "__main__":
    run()
