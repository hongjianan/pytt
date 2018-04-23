# encoding: utf-8
'''
Created on 2018年4月11日

@author: Hong
'''

 # 1. 可调用对象是一个函数
def application(environ, start_response):
 
   response_body = 'The request method was %s' % environ['REQUEST_METHOD']
 
   # HTTP response code and message
   status = '200 OK'
 
   # 应答的头部是一个列表，每对键值都必须是一个 tuple。
   response_headers = [('Content-Type', 'text/plain'),
                       ('Content-Length', str(len(response_body)))]
 
   # 调用服务器程序提供的 start_response，填入两个参数
   start_response(status, response_headers)
 
   # 返回必须是 iterable
   return [response_body]    
   
   
# 2. 可调用对象是一个类
class AppClass:
    """这里的可调用对象就是 AppClass 这个类，调用它就能生成可以迭代的结果。
        使用方法类似于： 
        for result in AppClass(env, start_response):
             do_somthing(result)
    """
 
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
 
    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"


# 3. 可调用对象是一个实例 
class AppClass:
    """这里的可调用对象就是 AppClass 的实例，使用方法类似于： 
        app = AppClass()
        for result in app(environ, start_response):
             do_somthing(result)
    """
 
    def __init__(self):
        pass
 
    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"
        
if __name__ == '__main__':
    pass