import time
import sys

def use_mem(l, int_cout):
    size = 0
    while size < int_cout:
        size += 4
        l.append(123456)
    

start = time.time()

mem_size_MB = int(sys.argv[1])
if (mem_size_MB > 4):
    mem_size_MB -= 4
else:
    mem_size_MB = 0

l = []
use_mem(l, mem_size_MB * 1024 * 1024 / 2)


use = time.time() - start
print("using time:", use)

time.sleep(100)
