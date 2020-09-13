#实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import timeit
def time(func,*args,**kargs):
    #return timeit.timeit(stmt=func)
    
    print(timeit.timeit(stmt=func))

@time    
def addone():
    return 1


print(addone())
#print(timeit.timeit(stmt=[i for i in range(10)]))