class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('Мяу-мяу')

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('Гав-гав')


puppy = Dog('Nike', 5)
print(f'name: {puppy.name}, age: {puppy.age}')
puppy.name = 'Tayson'
puppy.age = 3
print(f'new name: {puppy.name}, new age: {puppy.age}')
kitty = Cat('Conya', 1)
print(f'name: {kitty.name}, age: {kitty.age}')
kitty.age = 2
kitty.name = 'Lilly'
print(f'new name: {kitty.name}, new age: {kitty.age}')
print()
animals = [puppy, kitty]
for s in animals:
    s.make_sound()
