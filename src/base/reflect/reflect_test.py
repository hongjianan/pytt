# -*- coding: utf-8 -*-

def add(a, b):
    print('add(%s, %s)' % (a, b))
    return a + b

class Action:
    def dispatch(self, action, groupid, *args, **kwargs):
        try:
            func = getattr(self, action)
        except AttributeError:
            print('eeeee')
            raise
        return func(*args, **kwargs)
        
    def test(self, name, age):
        print('======test=====', name, age)
        

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
    

def call_func():
    fun = getattr(__name__, 'add')
    fun(1, 2)
    
def class_call():
    obj = Action()
    obj.dispatch('test1', 11, name='jason', age=23)

if __name__ == "__main__":
    # import_tt()
    # reflect_tt()
    # call_func()
    class_call()
    

