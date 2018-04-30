# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

import time
import threading

def single_count(max):
    begin = time.time()
    count = 0
    while count < max:
        count += 1
    using = time.time() - begin
    print('single_count using time', using)

   
def multi_count(nums, max):
    workers = [threading.Thread(target=single_count, args=(max,)) for x in range(nums)]
    
    begin = time.time()
    for worker in workers:
        worker.start()
    
    
    for worker in workers:
        worker.join()
        
    using = time.time() - begin
    print('multi_count using time', using)
    

if __name__ == '__main__':
#     single_count(1000 * 1000 * 100)
    multi_count(2, 1000 * 1000 * 100)