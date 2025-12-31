# Dependencies 
from abc import ABC, abstractmethod

# Class
# What is a class?
# > A class is a blueprint or template for creating objects.

class Example:
    pass 

e = Example()
print("Memory location of 'e'", e)

# Constractor
# What is a constractor?
# > A constractor runs autometically when an object is created and initializes the object.

# Types of constractor
# > Parameterized & Un-parameterized 

# Un-parameterized constructor 
class A:
    def __init__(self):
        pass 

a = A()
print("Memory location of 'a'", a)


# Parameterized constructor 
class Person:
    def __init__(self, name, age): # Self works as object
        self.name = name
        self.age = age 

p = Person("Ayanabha", 21)
print(f"My name is {p.name} & I am {p.age} years old.")


# Inheritance
# What is inheritance?
# > A class can reuse properties and methods from another class (parent class). 

# class Animal:
#     def animal_make_sound(self):
#         return "Barks"

# class Dog(Animal):
#     pass 

# d = Dog()
# print(f"Dogs, {d.animal_make_sound()}")


# Method Overloading 
# > Same method name but different behaviour using default arguments. 
class Test:
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print(a, b)
        elif a is not None:
            print(a) 
        else:
            print("No value")

t = Test()
t.show(5)
t.show(5, 10)
t.show()


# Method Overriding 
# > Child class changes the methid of parent class. 
# class Animal:
#     def animal_make_sound(self):
#         return "Barks"

# class Dog(Animal):
#     def animal_make_sound(self):
#         return "Ghaw Ghaw"

# animal = Animal()
# dog = Dog()
# print(f"A dog {animal.animal_make_sound()} but dogs {dog.animal_make_sound()}")


# Multiple Inheritance 
# > A class inherits from more tha one parent. 
class A:
    def a(self):
        return "Apple"

class B:
    def b(self):
        return "Ball"

class C(A, B):
    def c(self):
        return "Cat"
c = C()
print(c.a(), c.b(), c.c())


# Encapsulation
# What is encapsulation?
# > Hiding data inside the class using private variables. 

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Double underscore '__' for make 'balance' private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(5000)
print(f"Account Balance: {acc.get_balance()}")

# Properties 
# > Controlled access to variables using getter and setter. 
class Student:
    def __init__(self, s_name):
        self.__s_name = s_name

    @property
    def s_name(self):
        return self.__s_name
    
    @s_name.setter
    def s_name(self, value):
        self.__s_name = value

s = Student("Rahul") 
print("Student:", s.s_name)
s.s_name = "Rohit"
print("Updated Student:", s.s_name)


# Class variable vs Instance variable
# > Class variable is shared... instence variable is different per object. 

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1 

c1 = Counter()
c2 = Counter()
print("Objects created:", Counter.count)


# Classmethod and Staticmethod
# > Classmethod uses class data
# > Staticmethod is a normal helper method. 

class MathUtils:
    pi = 3.14

    @classmethod
    def circle_area(cls, r):
        return cls.pi * r * r 

    @staticmethod
    def add(a, b):
        return a + b  

print("Circle area:", MathUtils.circle_area(5))
print("Add", MathUtils.add(10, 20))


# Polymorphism  
# What is polymorphism?
# > Sae method name behaves differently in different classes. 

class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

def animal_sound(obg):
    print(obg.speak())

animal_sound(Cat())
animal_sound(Dog())


# Abstraction 
# What is abstraction?
# > Hiding implementatuon details, only showing necessary methods. 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side 

sq = Square(4)
print("Square area:", sq.area())


# Composition
# What is composition?
# > Creating complex objects using other objects. 

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return self.engine.start() + " ... Car moving"

car = Car()
print(car.drive())





# All Class concept done..... 













