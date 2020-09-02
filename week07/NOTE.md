学习笔记
class Human(object):

    # 静态字段

    live = True



    def __init__(self, name):

        # 普通字段

        self.name = name



man = Human('Adam')

woman = Human('Eve')



# 有静态字段,live属性

Human.__dict__

# 有普通字段,name属性

man.__dict__



# 实例可以使用普通字段也可以使用静态字段

man.name

man.live = False

# 查看实例属性

man.__dict__ #普通字段有live变量

man.live

woman.live



# 类可以使用静态字段

Human.live



# 可以为类添加静态字段

Human.newattr = 1

dir(Human)

Human.__dict__



# 内置类型不能增加属性和方法

setattr(list, 'newattr', 'value')

# TypeError



# 显示object类的所有子类

print( ().__class__.__bases__[0].__subclasses__() )



class Human2(object):

    # 人为约定不可修改

    _age = 0



    # 私有属性

    __fly = False



    # 魔术方法，不会自动改名

    # 如 __init__  ，这个是初始化函数
__new__,  这个是构造函数





# 自动改名机制

Human2.__dict__




# 让实例的方法成为类的方法
class Kls1(object):
    bar = 1
    def foo(self):
        print('in foo')
    # 使用类属性、方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()

Kls1.class_foo()


#########################
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake
    

s = Story('anyone')
# get_apple_to_eve 是bound方法，查找顺序是先找s的__dict__是否有get_apple_to_eve,如果没有，查类Story
print(s.get_apple_to_eve)
# 类和实例都可以使用
print(s.get_apple_to_eve())
print(Story.get_apple_to_eve())
# print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)))
# print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)) == s.get_apple_to_eve)


##############
class Kls2():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me = Kls2('wilson','yin')
me.print_name()

# 输入改为  wilson-yin

解决方法1: 修改 __init__()
解决方法2: 增加 __new__() 构造函数
解决方法3: 增加 提前处理的函数

def pre_name(obj,name):
    fname, lname = name.split('-')
    return obj(fname, lname)

me2 = pre_name(Kls2, 'wilson-yin')
me2.print_name()


##############
class Kls3():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @classmethod
    def pre_name(cls,name):
        fname, lname = name.split('-')
        return cls(fname, lname)
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me3 = Kls3.pre_name('wilson-yin')
me3.print_name()

# 思考： 如果用户输入的是 "yin,wilson" 怎样处理



'''
类方法用在模拟java定义多个构造函数的情况。
由于python类中只能有一个初始化方法，不能按照不同的情况初始化类。
'''
class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book

book1 = Book("python")
book2 = Book.create("python and django")
print(book1.title)
print(book2.title)



############
class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print(f'calling {cls} ,{value}')
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

Apple.set(100)
# calling <class '__main__.Apple'> ,100
Orange.set(200)
# calling <class '__main__.Orange'> ,200
org=Orange()
org.set(300)
# calling <class '__main__.Orange'> ,300
Apple.print_total()
# 100
# 140735711069824
# 140735711073024
Orange.print_total() 
# 300
# 140735711069824
# 1998089714064
# >>>


import datetime

class Story(object):

    snake = 'Python'

    def __init__(self, name):

        self.name = name

    # 静态的方法

    @staticmethod

    def god_come_go():

        if datetime.datetime.now().month % 2 :

             print('god is coming')

    

Story.god_come_go()



# 静态方法可以由类直接调用，作用：值的转换，判断等

# 因为不传入self 也不传入 cls ，所以不能使用类属性和实例属性

属性的处理


# GOD
class Human(object):  
    # 接收参数  
    def __init__(self, name):
        self.name = name

h1 = Human('Adam')
h2 = Human('Eve')


# 对实例属性做修改
h1.name = 'python'

# 对实例属性查询
h1.name

# 删除实例属性
del h1.name

# AttributeError，访问不存在的属性
# 由__getattribute__(self,name)抛出
h1.name



###################
class Human2(object):  
    """
    getattribute对任意读取的属性进行截获
    """  
    def __init__(self):
        self.age = 18
    def __getattribute__(self,item):
        print(f' __getattribute__ called item:{item}')

h1 = Human2()

h1.age
h1.noattr




class Human2(object):  

    """

    拦截已存在的属性

    """  

    def __init__(self):

        self.age = 18

    def __getattribute__(self,item):

        print(f' __getattribute__ called item:{item}')

        return super().__getattribute__(item)

h1 = Human2()



print(h1.age)

# 存在的属性返回取值

print(h1.noattr)

# 不存在的属性返回 AttributeError


class Human2(object):    

    def __getattribute__(self, item):

        """

        将不存在的属性设置为100并返回,模拟getattr行为

        """

        print('Human2:__getattribute__')

        try:

            return super().__getattribute__(item)

        except Exception as e:

            self.__dict__[item] = 100

            return 100

h1 = Human2()



print(h1.noattr)

class Human2(object):  

    """

    属性不在实例的__dict__中,__getattr__被调用

    """

    def __init__(self):

        self.age = 18



    def __getattr__(self, item): 

        print(f' __getattr__ called item:{item}')

        # 不存在的属性返回默认值 'OK'

        return 'OK'



h1 = Human2()



print(h1.age)

print(h1.noattr)



class Human2(object):  

    def __init__(self):

        self.age = 18



    def __getattr__(self, item): 

        # 对指定属性做处理:fly属性返回'superman',其他属性返回None

        self.item = item

        if self.item == 'fly':

            return 'superman'





h1 = Human2()



print(h1.age)

print(h1.fly)

print(h1.noattr)


class Human2(object):    

    """

    同时存在的调用顺序

    """

    def __init__(self):

        self.age = 18



    def __getattr__(self, item): 



        print('Human2:__getattr__')

        return 'Err 404 ,你请求的参数不存在'



    def __getattribute__(self, item):

        print('Human2:__getattribute__')

        return super().__getattribute__(item)



h1 = Human2()



# 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__

print(h1.age)

print(h1.noattr)

# 注意输出，noattr的调用顺序


property


class Desc(object):

    """

    通过打印来展示描述器的访问流程

    """

    def __init__(self, name):

        self.name = name

    

    def __get__(self, instance, owner):

        print(f'__get__{instance} {owner}')

        return self.name



    def __set__(self, instance, value):

        print(f'__set__{instance} {value}')

        self.name = value



    def __delete__(self, instance):

        print(f'__delete__{instance}')

        del self.name



class MyObj(object):

    a = Desc('aaa')

    b = Desc('bbb')



my_object = MyObj()

print(my_object.a)



my_object.a = 456

print(my_object.a)
输出：
__get__<__main__.MyObj object at 0x00000247C103E4A8> <class '__main__.MyObj'>
aaa
__set__<__main__.MyObj object at 0x00000247C103E4A8> 456
__get__<__main__.MyObj object at 0x00000247C103E4A8> <class '__main__.MyObj'>
456



# GOD

class Human(object):

    def __init__(self, name):

        self.name = name



    # 将方法封装成属性

    @property                 #默认只有只读功能

    def gender(self):

        return 'M'



h1 = Human('Adam')

h2 = Human('Eve')

h1.gender



# AttributeError: 

h2.gender = 'F'







#################

# GOD

class Human2(object):

    def __init__(self):

        self._gender = None

    # 将方法封装成属性

    @property

    def gender2(self):

        print(self._gender)



    # 支持修改

    @gender2.setter

    def gender2(self,value):

        self._gender = value



    # 支持删除

    @gender2.deleter

    def gender2(self):

        del self._gender





h = Human2()

h.gender2 = 'F'

h.gender2

del h.gender2

# 另一种property写法

# gender  = property(get_, set_, del_, 'other property')







# 被装饰函数建议使用相同的gender2

# 使用setter 并不能真正意义上实现无法写入，gender被改名为 _Article__gender





# property本质并不是函数，而是特殊类（实现了数据描述符的类）

# 如果一个对象同时定义了__get__()和__set__()方法，则称为数据描述符，

# 如果仅定义了__get__()方法，则称为非数据描述符



# property的优点：

# 1 代码更简洁，可读性、可维护性更强。

# 2 更好的管理属性的访问。

# 3 控制属性访问权限，提高数据安全性。





# property 纯python实现



class Property(object):

    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):

        self.fget = fget

        self.fset = fset

        self.fdel = fdel

        if doc is None and fget is not None:

            doc = fget.__doc__

            self.__doc__ = doc

    

    def __get__(self, obj, objtype=None):

        if obj is None:

            return self

        if self.fget is None:

            raise AttributeError("unreadable attribute")

        return self.fget(obj)



    def __set__(self, obj, value):

        if self.fset is None:

            raise AttributeError("can't set attribute")

        self.fset(obj, value)



    def __delete__(self, obj):

        if self.fdel is None:

            raise AttributeError("can't delete attribute")

        self.fdel(obj)



    def getter(self, fget):

        return type(self)(fget, self.fset, self.fdel, self.__doc__)



    def setter(self, fset):

        return type(self)(self.fget, fset, self.fdel, self.__doc__)



    def deleter(self, fdel):

        return type(self)(self.fget, self.fset, fdel, self.__doc__)



#ORM(flask.ext.sqlalchemy)
# 一个表记录一个节点的心跳更新
# 通过一个属性来获取节点是否可用，而不用写复杂的查询语句
class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated_at = db.Column(db.DateTime) # 节点最后心跳时间
    state = db.Column(db.Integer, nullable=False) # 节点是否禁用

    @property
    def is_active(self):
        if(datetime.datetime.now() - self.updated_at).secondes > 60 \
            and self.vm_state == 0:
            return False
        return True

#########################
# 限制传入的类型和范围（整数，且满足18-65）
class Age(object):
    def __init__(self, default_age = 18):
        self.age_range = range(18,66)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_age)
    
    def __set__(self, isinstance, value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')

        self.data[isinstance] = value

class Student(object):
    age = Age()

if __name__ == '__main__':
    s1 = Student()
    s1.age = 30
    s1.age = 100

############################
# 固定部分传递的参数
def xxyun_client(apitype, ak, sk, region='cn-beijing-3'):
    s = get_session()
    client = s.create_client(
        apitype,
        region,
        user_ssl = True,
        access_key =ak,
        secret_access_key =sk
    )
    return client


class XXYunBase(object):
    def __init__(self, account):
        self.account = account
        self.ak = self.account.ak
        self.sk = self.account.sk
    
    @property
    def eip_(self):
        return partial(xxyun_client, 'eip', self.ak, self.sk)
    
    @property
    def vpc_(self):
        return partial(xxyun_client, 'vpc', self.ak, self.sk)



##################
@property
def current_state(self):
    instance_state = {
       1: '运行',
       2: '离线',
       3: '下线',

   } 
    if(time_diff.seconds) >= 300:
       return instance_state[2]

    if self.state in range(10):
        return instance_state.get(self.state, '其他')
    return None 



from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from manage import db
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)


# 使用装饰器完成password的读取和写入功能分离
    @property
    def password(self):
        return None
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
  
    def is_active(self):
        return True


继承

# 父类
class People(object):
    def __init__(self, name):
        self.gene = 'XY'
        # 假设人人都有名字
        self.name = name
    def walk(self):
        print('I can walk')

# 子类
class Man(People):
    def __init__(self,name):
        # 找到Man的父类People，把类People的对象转换为类Man的对象
        super().__init__(name)

    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self,name):
        super().__init__(name)
    def shopping(self):
        print('buy buy buy')

p1 = Man('Adam')
p2 = Woman('Eve')

# 问题1 gene有没有被继承？
# super(Man,self).__init__()
p1.gene

# 问题2 People的父类是谁？
# object 与 type
print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)
# type元类由type自身创建，object类由元类type创建
# type类继承了object类

# 问题3 能否实现多重层级继承

# 问题4 能否实现多个父类同时继承 
class Son(Man, Woman):
    pass


# 新的问题： 继承顺序
# 钻石继承

# 钻石继承
class BaseClass(object):
    num_base_calls = 0
    def call_me(self):
        print ("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        print ("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(object):
    num_right_calls = 0
    def call_me(self):
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass,RightSubclass):
    pass

a = Subclass()
a.call_me()

print(Subclass.mro())
# 广度优先， 另外Python3 中不加(object)也是新式类，但是为了代码不会误运行在python2下产生意外结果，仍然建议增加
# >>> Subclass.mro()
# [<class '__main__.Subclass'>, <class '__main__.LeftSubclass'>, <class '__main__.RightSubclass'>, <class '__main__.BaseClass'>, <class 'object'>]

#  修改RightSubclass 的 父类为 Object
# >>> Subclass.mro()
# [<class '__main__.Subclass'>, <class '__main__.LeftSubclass'>, <class '__main__.BaseClass'>, <class '__main__.RightSubclass'>, <class 'object'>]








设计原则



# 装饰器实现单实例模式
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton 
class MyClass:
    pass

m1 = MyClass()
m2 = MyClass()
print(id(m1))
print(id(m2))


##################
# __new__ 与 __init__ 的关系
class Foo(object):
    def __new__(cls, name):
        print('trace __new__')
        return super().__new__(cls)
    
    def __init__(self, name):
        print('trace __init__')
        super().__init__()
        self.name = name

bar = Foo('test')
bar.name


#相当于在执行下面的操作
bar = Foo.__new__(Foo, 'test')
if isinstance(bar, Foo):
    Foo.__init__(bar, 'test')

############################
# __new__ 方式实现单例模式
class Singleton2(object):
	__isinstance = False  # 默认没有被实例化
	def __new__(cls, *args, **kwargs):
		if cls.__isinstance:  
			return cls.__isinstance  # 返回实例化对象
		cls.__isinstance = object.__new__(cls)  # 实例化
		return cls.__isinstance


# object定义了一个名为Singleton的单例，它满足单例的3个需求：
# 一是只能有一个实例；
# 二是它必须自行创建这个实例；
# 三是它必须自行向整个系统提供这个实例。

class _Singleton(object):
    pass
Singleton = _Singleton()
del _Singleton 
another = Singleton.__class__() # 没用，绕过




# __new__

#方法1,实现__new__方法
#并在将一个类的实例绑定到类变量_instance上,
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
#如果cls._instance不为None,直接返回cls._instance
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kargs)
        return cls._instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)

# 解决并发，引入带锁版
import threading
class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()
    def __new__(cls, *args, **kargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs: ## double check locking
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()


# 利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现。
# 但这个方案并不完美，至少还有以下两个问题：
# ·如果Singleton的子类重载了__new__()方法，会覆盖或者干扰Singleton类中__new__()的执行，
# 虽然这种情况出现的概率极小，但不可忽视。
# ·如果子类有__init__()方法，那么每次实例化该Singleton的时候，
# __init__()都会被调用到，这显然是不应该的，__init__()只应该在创建实例的时候被调用一次。
# 这两个问题当然可以解决，比如通过文档告知其他程序员，子类化Singleton的时候，请务必记得调用父类的__new__()方法；
# 而第二个问题也可以通过偷偷地替换掉__init__()方法来确保它只调用一次。
# 但是，为了实现一个单例，做大量的、水面之下的工作让人感觉相当不Pythonic。
# 这也引起了Python社区的反思，有人开始重新审视Python的语法元素，发现模块采用的其实是天然的单例的实现方式。
# ·所有的变量都会绑定到模块。
# ·模块只初始化一次。
# ·import机制是线程安全的（保证了在并发状态下模块也只有一个实例）。
# 当我们想要实现一个游戏世界时，只需简单地创建World.py就可以了。

# World.py
import Sun
def run():
    while True:
        Sun.rise()
        Sun.set()

# main.py
import World
World.run()


工厂模式
class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Man(Human):
    def __init__(self, name):
        print(f'Hi,man {name}')

class Woman(Human):
    def __init__(self, name):
        print(f'Hi,woman {name}')

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)
        else:
            pass

if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Adam", "M")



# 返回在函数内动态创建的类
def factory2(func):
    class klass: pass
    #setattr需要三个参数:对象、key、value
    setattr(klass, func.__name__, func)
    return klass

def say_foo(self): 
    print('bar')

Foo = factory2(say_foo)
foo = Foo()
foo.say_foo()


元类


