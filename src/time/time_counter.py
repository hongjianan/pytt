# coding: UTF-8

import time

class TimerCounter:
    def __init__(self):
        self.start = time.time()

    def __del__(self):
        use = time.time() - self.start
        print("time use", use)

def run():
    counter = TimerCounter()
    time.sleep(1)
    counter = None

    time.sleep(1)


if __name__ == "__main__":
    run()

