from abc import ABC, abstractmethod

#Abstraction

class WashinMachine:
    
    def start_washing_machine(self):
        self.fill_water()
        self.add_detergent()
        self.rotate_drum()

    def fill_water(self):
        print("Filling water...")

    def add_detergent(self):
        print("Adding detergent...")

    def rotate_drum(self):
        print("Rotating drum...")


ws = WashinMachine()
ws.start_washing_machine()

print('------------------------------------------------------')

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass # no body here, child must define it


class Dog(Animal):

    def make_sound(self):
        print('Bhou Baou')
    

class Cat(Animal):

    def make_sound(self):
        print('mau mau')


dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# Incapsulation

class Person:

    def __init__(self):
        self.name = 'Gaurav'    # public
        self._age = 25          # protected
        self.__salary = 50000   # private
    

    def get_salary(self):
        return self.__salary


p = Person()
print(p.name)   # can access
print(p._age)   # possible, but should be avoided
# print(p.__salary)   # AttributeError

print(p.get_salary())
print(p._Person__salary)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# INHERITANCE

class Animal:

    zoo_name = 'Abc Zoo' 

    def __init__(self, age):
        self.age = age

    def speak(self):
        print('animal speaks')

class Lion(Animal):

    def __init__(self, age):
        super().__init__(age)

    def bark(self):
        print('Dhishoom Dhishoom')


lion = Lion(12)
print(lion.zoo_name)
print(lion.age)
lion.speak()
lion.bark()

class A:
    def showA(self):
        print("This is class A")

class B(A):
    def showB(self):
        print("This is class B")

class C(B):
    def showC(self):
        print('This is class C')


c = C()
c.showA()
c.showB()
c.showC()


class Father:
    def skill(self):
        print("Good at driving")

class Mother:
    def talent(self):
        print("Good at cooking")

    def skill(self):
        print("Good at yelling")

        
class Child(Father, Mother):
    def hobby(self):
        print("Loves painting")


c = Child()
c.skill()
c.talent()
c.hobby()


class Teacher:
    def show(self):
        print("I am the Parent")

class Student1(Teacher):
    pass

class Student2(Teacher):
    pass

s1 = Student1()
s2 = Student2()
s1.show()
s2.show()


class Employee:
    def status(self):
        print("Emplyee is working")

class Emp1(Employee):
    def status(self):     # overriding parent method
        print("Emp1 is on leave")

e = Emp1()
e.status()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#Polymorphism

class Test1:
    def speak(self):
       print("Bark")

class Test2:
    def speak(self):
        print("Meow")

t1 = Test1()
t2 = Test2()
t1.speak()
t2.speak()


class Sport:

    def greet(self):
        print('Thhis is sprot')

class Cricket(Sport):

    def greet(self):
        print('This sport is cricket')


c = Cricket()
c.greet()  # This sport is cricket




