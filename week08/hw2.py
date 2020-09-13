#自定义一个 python 函数，实现 map() 函数的功能。  map(fun,iterable)

def MyMap(func, my_iter):
    result = iter([func(i) for i in my_iter])
    return result

def addone(x):
    return x + 1


ret = MyMap(addone, [1,2,3])
for i in ret:
    print(i)

