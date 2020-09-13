学习笔记


变量赋值
传的是对象本身：不可变数据类型
传的是对象的引用：可变数据类型
这些数据类型都是对象，可以理解成箱子，变量是便签，赋值理解为贴便签

# 问题1: a、b、c三个id是否相同

a = 123

b = 123

c = a

print(id(a))

print(id(b))

print(id(c))
相同





#############

# 问题2: a、b、c的值分别是多少

a = 456

print(id(a))

c = 789

c = b = a
相同  789





#############

# 问题3: x、y的值分别是什么

x = [1,2,3]

y = x

x.append(4)

print(x)

print(y)

[1, 2, 3, 4]
[1, 2, 3, 4]





#############

# 问题4: a、b的值分别是多少

a = [1, 2, 3]

b = a

a = [4, 5, 6]


a	[4, 5, 6]
b	[1, 2, 3]



#############

# 问题5: a、b的值分别是多少

a = [1, 2, 3]

b = a

a[0],a[1],a[2] = 4, 5, 6

相同	[4, 5, 6]


容器序列的深浅拷贝
# 容器序列的拷贝问题

old_list = [ i for i in range(1, 11)]

new_list1 = old_list
new_list2 = list(old_list)  #产生新列表

# 切片操作
new_list3 = old_list[:]   #产生新列表

# 嵌套对象
old_list.append([11, 12])



import copy
new_list4 = copy.copy(old_list)
new_list5 = copy.deepcopy(old_list)

assert new_list4 == new_list5 #True
assert new_list4 is new_list5 #False AssertionError

old_list[10][0] = 13
print(new_list4)
print(new_list5)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]   
浅拷贝只拷贝其引用地址，深拷贝不仅拷贝引用也拷贝引用所指向的对象，因此深拷贝得到的对象和原对象是相互独立的

# 命名元组
from collections import namedtuple
Point = namedtuple('Ponit', ['x','y'])
p = Point(10, y=20)
p.x + p.y
p[0] + p[1]
x, y = p


from collections import Counter
mystring = ['a','b','c','d','d','d','d','c','c','e']
# 取得频率最高的前三个值
cnt = Counter(mystring)
cnt.most_common(3)
cnt['b']


# 双向队列
from collections import deque
d = deque('uvw')
d.append('xyz')
d.appendleft('rst')



import numpy as np
'''
计算欧式距离
'''

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

op1 = np.sqrt(np.sum(np.square(vector1-vector2)))
op2 = np.linalg.norm(vector1-vector2)


from collections import namedtuple
from math import sqrt
Point = namedtuple('Ponit', ['x','y','z'])

class Vector(Point):
    def __init__(self, p1, p2, p3):
        super(Vector).__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def __sub__(self, other):
        tmp = (self.p1 - other.p1)**2+(self.p2 - other.p2)**2+(self.p3 - other.p3)**2
        return sqrt(tmp)

p1 = Vector(1, 2, 3)
p2 = Vector(4, 5, 6)

p1-p2








# L G

x = 'Global'

def func2():

    x = 'Enclosing'



    def func3():

        x = 'Local'



        print (x)

    func3()

print(x)

func2()







# E

x = 'Global'

def func4():

    x = 'Enclosing'

    def func5():

        return x

    return func5



var = func4()

print( var() )





# B

print (dir (__builtins__) )


# 偏函数

def add(x, y):

    return x + y



import functools

add_1 = functools.partial(add, 1)

add_1(10)



import itertools

g = itertools.count()

next(g)

next(g)

auto_add_1 = functools.partial(next, g)   

auto_add_1()    #之后每次调用相当于next(g)




# 内部函数对外部函数作用域里变量的引用（非全局变量）则称内部函数为闭包

def counter(start=0):
   count=[start]
   def incr():
       count[0]+=1
       return count[0]
   return incr

c1=counter(10)

print(c1())
# 结果：11
print(c1())
# 结果：12

# nonlocal访问外部函数的局部变量
# 注意start的位置，return的作用域和函数内的作用域不同
def counter2(start=0):
    def incr():
        nonlocal start
        start+=1
        return start
    return incr
c1=counter2(5)
print(c1())
print(c1())

c2=counter2(50)
print(c2())
print(c2())

print(c1())
print(c1())

print(c2())
print(c2())




# PEP 318 装饰器  PEP-3129 类装饰器

# 前置问题
def func1():
    pass
a=func1
b=func1()

# func1 表示函数
# func1() 表示执行函数

############################
# 装饰器, @ 语法糖
@decorate   
def func2():
    print('do sth')

# 等效于下面
def func2():
    print('do sth')
func2 = decorate(func2)

#############################







# 装饰器在模块导入的时候自动运行
# testmodule.py
def decorate(func):
    print('running in modlue')
    def inner():
        return func()
    return inner

@decorate
def func2():
    pass

# test.py
import testmodule
# from testmodule import func2


# 用在哪里
# Flask 的装饰器是怎么用的？
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>hello world </h1>'

# app.add_url_rule('/', 'index')

if __name__ == '__main__':
   app.run(debug=True)



# 注册
@route('index',methods=['GET','POST'])
def static_html():
    return  render_template('index.html')

# 等效于
static_html = route('index',methods=['GET','POST'])(static_html)()


def route(rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", None)
        # 使用类似字典的结构以'index'为key 以 method static_html  其他参数为value存储绑定关系
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator

###############################

# 包装
def html(func):
    def decorator():
        return f'<html>{func()}</html>'
    return decorator

def body(func):
    def decorator():
        return f'<body>{func()}</body>'
    return decorator

@html
@body
def content():
    return 'hello world'

content()

<html><body>hello world</body></html>

被修饰函数带参数和返回值的处理
# 被修饰函数带参数
def outer(func):
    def inner(a,b):
        print(f'inner: {func.__name__}')
        print(a,b)
        func(a,b)
    return inner

@outer
def foo(a,b):
    print(a+b)
    print(f'foo: {foo.__name__}')
    
    
foo(1,2)
输出
inner:foo
1,2
3
foo:inner  
#注意
1.原函数被替换为装饰器的内部函数
2.原函数有几个参数，装饰器的内部函数也要对应

foo.__name__

############################################

# 被修饰函数带不定长参数


def outer2(func):
    def inner2(*args,**kwargs):
        func(*args,**kwargs)
    return inner2

@outer2
def foo2(a,b,c):
    print(a+b+c)
    
foo2(1,3,5)


############################################

# 被修饰函数带返回值

def outer3(func):
    def inner3(*args,**kwargs):
        ###
        ret = func(*args,**kwargs)
        ###
        return ret
    return inner3

@outer3
def foo3(a,b,c):
    return (a+b+c)
    
print(foo3(1,3,5))

# 装饰器带参数 

def outer_arg(bar):
    def outer(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            print(bar)
            return ret
        return inner
    return outer

# 相当于outer_arg('foo_arg')(foo)()
@outer_arg('foo_arg')
def foo(a,b,c):
    return (a+b+c)
    
print(foo(1,3,5))

############################################

# 装饰器堆叠

@classmethod
@synchronized(lock)
def foo(cls):
    pass


def foo(cls):
    pass
foo2 = synchronized(lock)(foo)
foo3 = classmethod(foo2)
foo = foo3


python内置装饰器
########################
# 内置的装饰方法函数

# functools.wraps
# @wraps接受一个函数来进行装饰
# 并加入了复制函数名称、注释文档、参数列表等等的功能
# 在装饰器里面可以访问在装饰之前的函数的属性
# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 用于在定义包装器函数时发起调用 update_wrapper() 作为函数装饰器。 
# 它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)。

from time import ctime,sleep
from functools import wraps
def outer_arg(bar):
    def outer(func):
        # 结构不变增加wraps
        @wraps(func)
        def inner(*args,**kwargs):
            print("%s called at %s"%(func.__name__,ctime()))
            ret = func(*args,**kwargs)
            print(bar)
            return ret
        return inner
    return outer

@outer_arg('foo_arg')
def foo(a,b,c):
    """  __doc__  """
    return (a+b+c)
    
print(foo.__name__)


########################
# flask 使用@wraps()的案例
from functools import wraps
 
def requires_auth(func):
    @wraps(func)
    def auth_method(*args, **kwargs):
        if not auth:
            authenticate()
        return func(*args, **kwargs)
    return auth_method

@requires_auth
def func_demo():
    pass

########################

from functools import wraps
 
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator
 
@logit()
def myfunc1():
    pass
 
myfunc1()
# Output: myfunc1 was called
 
@logit(logfile='func2.log')
def myfunc2():
    pass
 
myfunc2()

# Output: myfunc2 was called



##########################
# 可以使用wrapt包替代@wraps
# # wrapt包 https://wrapt.readthedocs.io/en/latest/quick-start.html
#  @wrapt.decorator
#  def wrapper(func, instance, args, kwargs):

import wrapt

def with_arguments(myarg1, myarg2):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        return wrapped(*args, **kwargs)
    return wrapper

@with_arguments(1, 2)
def function():
    pass


# functools.lru_cache
# 《fluent python》的例子
# functools.lru_cache(maxsize=128, typed=False)有两个可选参数
# maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放
# typed若为True，则会把不同的参数类型得到的结果分开保存
import functools
@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    import timeit
    print(timeit.timeit("fibonacci(6)", setup="from __main__ import fibonacci"))



# Python 2.6 开始添加类装饰器
from functools import wraps

class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)
    
    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + " was called"
            print(func_name)
            return func(*args, **kwargs)
        return wrapped_function

def myfunc():
    pass

MyClass(100)(myfunc)()
# 其他经常用在类装饰器的python自带装饰器
# classmethod
# staticmethod
# property


# 另一个示例
class Count(object):
    def __init__(self,func):
        self._func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kargs):
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')
        return self._func(*args, **kargs)

@Count
def example():
    print('hello')

example()
print(type(example))


# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)
            
        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print("run times", self.times)
            self.wrapped.display()
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number
    # 重写display
    def display(self):
        print("number is",self.number)

six = MyClass(6)
for i in range(5):
    six.display()


# 官方文档装饰器的其他用途举例

# 向一个函数添加属性
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate

@attrs(versionadded="2.2",
       author="Guido van Rossum")
def mymethod(f):
    pass

##############################

# 函数参数观察器
import functools
def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function
@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)

greet('better','me')


############################################

# Python3.7 引入 Data Class  PEP557

class MyClass:
    def __init__(self, var_a, var_b):
        self.var_a = var_a
        self.var_b = var_b

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False
        return (self.var_a, self.var_b) == (other.var_a, other.var_b)
        
var3 = MyClass('x','y')
var4 = MyClass('x','y')

var3 == var4

from dataclasses import dataclass
@dataclass
class MyClass:
    var_a: str
    var_b: str

var_1 = MyClass('x','y')
var_2 = MyClass('x','y')

# 不用在类中重新封装 __eq__

var_1 == var_2
# 存在的问题: var_a var_b不能作为类属性访问













##########################



# 如下的类装饰器实现了一个用于类实例属性的Private声明
# 属性存储在一个实例上，或者从其一个类继承而来
# 不接受从装饰的类的外部对这样的属性的获取和修改访问
# 但是，仍然允许类自身在其方法中自由地访问那些名称
# 类似于Java中的private属性

traceMe = False
def trace(*args):
    if traceMe:
        print('['+ ' '.join(map(str,args))+ ']')

def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self,*args,**kargs):
                self.wrapped = aClass(*args,**kargs)
            def __getattr__(self,attr):
                trace('get:',attr)
                if attr in privates:
                    raise TypeError('private attribute fetch:'+attr)
                else:
                    return getattr(self.wrapped,attr)
            def __setattr__(self,attr,value):
                trace('set:',attr,value)
                if attr == 'wrapped': # 这里捕捉对wrapped的赋值
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change:'+attr)
                else: # 这里捕捉对wrapped.attr的赋值
                    setattr(self.wrapped,attr,value)
        return onInstance
    return onDecorator

if __name__ == '__main__':
    traceMe = True

    @Private('data','size')
    class Doubler:
        def __init__(self,label,start):
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s'%(self.label,self.data))

    X = Doubler('X is',[1,2,3])
    Y = Doubler('Y is',[-10,-20,-30])
    print(X.label)
    X.display()
    X.double()
    X.display()
    print(Y.label)
    Y.display()
    Y.double()
    Y.label = 'Spam'
    Y.display()

    # 这些访问都会引发异常
    print(X.size())
    print(X.data)
    X.data = [1,1,1]
    X.size = lambda S:0
    print(Y.data)
    print(Y.size())

# 这个示例运用了装饰器参数等语法，稍微有些复杂，运行结果如下：
# [set: wrapped <__main__.Doubler object at 0x03421F10>]
# [set: wrapped <__main__.Doubler object at 0x031B7470>]
# [get: label]
# X is
# [get: display]
# X is => [1, 2, 3]
# [get: double]
# [get: display]
# X is => [2, 4, 6]
# [get: label]
# Y is
# [get: display]
# Y is => [-10, -20, -30]
# [get: double]
# [set: label Spam]
# [get: display]

对象协议






生成器








alist = [1, 2, 3, 4, 5]
hasattr( alist, '__iter__' )  # True       
hasattr( alist, '__next__' )  # False

for i in  alist:
    print(i)

# 结论一  列表是可迭代对象，或称作可迭代（iterable）,
#         不是迭代器（iterator）

# __iter__方法是 iter() 函数所对应的魔法方法，
# __next__方法是 next() 函数所对应的魔法方法

###########################

g = ( i for i in range(5))
g  #<generator object>

hasattr( g, '__iter__' )  # True    
hasattr( g, '__next__' )  # True

g.__next__()
next(g)
for i in g:
    print(i)

# 结论二 生成器实现完整的迭代器协议


##############################
# 类实现完整的迭代器协议

class SampleIterator:
    def __iter__(self):
        return self

    def __next__(self):
        # Not The End
        if ...:
            return ...
        # Reach The End
        else:
            raise StopIteration

# 函数实现完整的迭代器协议
def SampleGenerator():
    yield ...
    yield ...
    yield ...  # yield语句
# 只要一个函数的定义中出现了 yield 关键词，则此函数将不再是一个函数，
# 而成为一个“生成器构造函数”，调用此构造函数即可产生一个生成器对象。



###################
# check iter
def check_iterator(obj):
    if hasattr( obj, '__iter__' ):  
        if hasattr( obj, '__next__' ):
            print(f'{obj} is a iterator') # 完整迭代器协议
        else:
            print(f'{obj} is a iterable') # 可迭代对象
    else:
        print(f'{obj} can not iterable') # 不可迭代

def func1():
    yield range(5)

check_iterator(func1)
check_iterator(func1())

# 结论三： 有yield的函数是迭代器，执行yield语句之后才变成生成器构造函数

# itertools的三个常见无限迭代器
import itertools

count = itertools.count()  # 计数器
next(count)
next(count)
next(count)


###############
cycle = itertools.cycle( ('yes', 'no') ) # 循环遍历
next(cycle)
next(cycle)
next(cycle)

###############
repeat = itertools.repeat(10, times=2)  # 重复
next(repeat)
next(repeat)
next(repeat)



################
# 有限迭代器
for j in itertools.chain('ABC',[1, 2, 3]) :
    print(j)

# Python3.3 引入了 yield from 
# PEP-380
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s = 'ABC'
t = [1, 2, 3]
list(chain(s, t))

def chain2(*iterables):
    for i in iterables:
        yield from i   # 替代内层循环

list(chain2(s, t))

# 迭代器有效性测试
a_dict = {'a':1, 'b':2}
a_dict_iter = iter(a_dict)

next(a_dict_iter)

a_dict['c']=3

next(a_dict_iter)
# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效

# 尾插入操作不会损坏指向当前元素的List迭代器,列表会自动变长


# 迭代器一旦耗尽，永久损坏
x = iter([ y for y in range(5)])
for i in x:
    i
x.__next__()

def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index
        print(f'jump is {jump}')
        if jump is None:
            jump = 1   # next() 或者 send(None)
        index += jump 
        print(f'index is {index}')

if __name__ == '__main__':
    iterator = jumping_range(5)
    print(next(iterator)) # 0
    print(iterator.send(2)) # 2
    print(next(iterator)) # 3
    print(iterator.send(-1)) # 2
    for x in iterator:
        print(x) # 3, 
        

# Python3.3之后引入了新语法 yield from
def ex1():
    yield 1
    yield 2
    return 3

def ex2():
    ex1_result = yield from ex1()
    print(f'ex1 : {ex1_result}')
    yield None

gen1 = ex1()
gen1.send(None) # 1
gen1.send(None) # 2
gen1.send(None) # send 执行到return 返回 StopIteration: 3

for i in ex2():
    print(i)
# 1
# 2
# ex1:3
# None





##########################
def bottom():
# Returning the yield lets the value that goes up the call stack to come right back
# down.
    return (yield 42)

def middle():
    return (yield from bottom())

def top():
    return (yield from middle())

# Get the generator.
gen = top()
value = next(gen)
print(value) # Prints '42'.
try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value
print(value) # Prints '84'