# -*- coding: utf-8 -*-

import time
import threading
import pika

local_key = threading.local()

def make_exchange(exchange, type):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = "192.168.1.131"))
    channel = connection.channel()
    channel.exchange_declare(exchange = exchange, exchange_type = type)
    return connection, channel


def producer(exchange, type, routing_key = ""):
    print("=== producer start ===")
    # global local_key
    local_key.v = routing_key

    conn, channel = make_exchange(exchange, type)

    for i in range(2):
        time.sleep(1)
        message = str(time.time())
        channel.basic_publish(exchange = exchange,
                              routing_key = routing_key,
                              body = message)
        print("--> send: %s" % message)

    conn.close()
    print("=== producer end ===")


def consumer(exchange, type, routing_keys = (None,)):
    def callback(ch, method, properties, body):
        print("tid[%s][%s] <-- recv: %s" % (threading.currentThread().ident, local_key.v, body))

    print("=== consumer start ===")
    # global local_key
    local_key.v = routing_keys

    conn, channel = make_exchange(exchange, type)
    queue = channel.queue_declare(exclusive = True)
    queue_name = queue.method.queue

    # 将匿名queue bind到交换机上, 在queue bind到交换机之前的数据将 全部丢弃
    for key in routing_keys:
        channel.queue_bind(exchange = exchange, queue = queue_name, routing_key = key)

    channel.basic_consume(callback, queue = queue_name, no_ack = True)
    channel.start_consuming()

    print("=== producer end ===")


def fanout():
    thds = []
    thds.append(threading.Thread(target = producer, args = ("logs", "fanout", )))
    thds.append(threading.Thread(target = consumer, args = ("logs", "fanout", )))
    thds.append(threading.Thread(target = consumer, args = ("logs", "fanout", )))

    for thd in thds:
        thd.start()

    for thd in thds:
        thd.join()


def direct():
    thds = []
    thds.append(threading.Thread(target = producer, args = ("direct_logs", "direct", "debug")))
    thds.append(threading.Thread(target = consumer, args = ("direct_logs", "direct", ("debug",))))
    thds.append(threading.Thread(target = consumer, args = ("direct_logs", "direct", ("debug", "error"))))
    thds.append(threading.Thread(target = consumer, args = ("direct_logs", "direct", ("error",))))

    for thd in thds:
        thd.start()

    for thd in thds:
        thd.join()


# topic 模糊匹配，a.b.c
# *: 1个单词
# #：0或者多个单词
def topic():
    thds = []
    thds.append(threading.Thread(target = producer, args = ("topic_logs", "topic", "debug.log.log")))
    thds.append(threading.Thread(target = consumer, args = ("topic_logs", "topic", ("debug.#",))))  # yes
    thds.append(threading.Thread(target = consumer, args = ("topic_logs", "topic", ("debug.*",))))  # no
    thds.append(threading.Thread(target = consumer, args = ("topic_logs", "topic", ("*.log.*",))))  # yes

    for thd in thds:
        thd.start()

    for thd in thds:
        thd.join()


def run():
    # fanout()
    # direct()
    topic()


if __name__ == "__main__":
    run()

