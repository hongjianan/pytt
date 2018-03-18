import time

def funA():
    while True:
        time.sleep(1)
        print("======funA======")
        yield()

def funB():
    while True:
        time.sleep(1)
        print("======funA======")
        next()

def tt():
    

if __name__ == '__main__':
    tt()

