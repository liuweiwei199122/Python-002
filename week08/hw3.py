#实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import time
from functools import reduce
def timer(func):
    def decorate(*args, **kargs):
        start = time.process_time()
        func(*args, **kargs)
        ret = time.process_time()- start
        return f'{ret: .5f}'
    return decorate
    
@timer  
def add(*args, **kargs):
    t = 0
    if len(args) == 0:
        return 0
    else:
        for i in args:
            t += i
        return t
    


print(add(1, 3))
