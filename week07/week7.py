from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, a_type, shape, character):
        self.name = name
        self.a_type = a_type
        self.shape = shape
        self.character = character
    
    @abstractmethod
    def is_terrible(self, a_type, shape, character):
        pass


class Cat(Animal):
    sound = 'miaomiaomiao'

    def __init__(self, name, a_type, shape, character):
        super().__init__(name, a_type, shape, character)

    @property
    def is_terrible(self):
        shape_dict = {"小":1, "中等":2, "大":3}
        if shape_dict[self.shape] >= 2 and self.a_type == '食肉' and self.character == '凶猛':
            return True
        else:
            return False

    @property
    def is_suit_pet(self):
        if self.is_terrible:
            return "不适合做宠物"
        else:
            return "适合做宠物"


class Dog(Animal):
    sound = 'wangwangwang'

    def __init__(self, name, a_type, shape, character):
        super().__init__(name, a_type, shape, character)

    @property
    def is_terrible(self):
        shape_dict = {"小":1, "中等":2, "大":3}
        if shape_dict[self.shape] >= 2 and self.a_type == '食肉' and self.character == '凶猛':
            return True
        else:
            return False

    @property
    def is_suit_pet(self):
        if self.is_terrible:
            return "不适合做宠物"
        else:
            return "适合做宠物"


class Zoo(object):
    
    def __init__(self,name,a_list=None):
        self.name = name
        if a_list is None:
            self.a_list = []
    def add_animal(self, Animal):      
        setattr(self,Animal.__class__.__name__,Animal)
        if Animal not in self.a_list:
            self.a_list.append(Animal)
        else:
            print(f"{Animal.__dict__['name']}已存在，请勿重复添加")
        

cat1 = Cat('大花猫 1', '食肉', '小', '温顺')

dog1 = Dog('大金狗 1', '食肉', '大', '凶猛')

z = Zoo('时间动物园')
z.add_animal(cat1)
z.add_animal(cat1)
z.add_animal(dog1)
print(hasattr(z, 'Cat'))


