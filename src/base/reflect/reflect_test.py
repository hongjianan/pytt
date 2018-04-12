# coding: UTF-8


def reflect_tt():
    time = __import__("time")
    ctime = getattr(time, "ctime")
    print(ctime, ctime())

    print(hasattr(time, "time"))
    delattr(time, "time")
    print(hasattr(time, "time"))

    setattr(time, "PRE_TIME", time.time())
    print(time.PRE_TIME)

    setattr(time, "get_pre_time", lambda : time.PRE_TIME)
    print(time.get_pre_time())


def import_tt():
    com = __import__("lib.test.com", fromlist = True)
    print(dir(com))


def run():
    import_tt()
    # reflect_tt()


if __name__ == "__main__":
    run()
    

