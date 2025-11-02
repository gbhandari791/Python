class Car:

    def __init__(self, name, model):
        self.name = name
        self.model = model
        print('Object is Initializing')

    def show_name(self):
        print(f'Car name is {self.name}')


my_car = Car('Gwagon', 'Top')
print(my_car.name)
print(my_car.model)

my_car.show_name()

print('--------------------------------------------------------------')

class Student:
    def __init__(self, name, marks):
        self.name = name       # instance variable
        self.marks = marks     # instance variable

    def display(self):         # instance method
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Gaurav", 85)
s2 = Student("Rahul", 90)

s1.display()
s2.display()

print('--------------------------------------------------------------')

class Teacher:

    school_name = 'ABC Public School'  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def chage_school(cls, new_name):
        cls.school_name = new_name  # modifying class variable

    def show(self):
         print(f"Name: {self.name}, School: {Teacher.school_name}")


teacher = Teacher("Test Teacher")
print(Teacher.school_name)
teacher.show()
Teacher.chage_school('XYZ Public School')
print(Teacher.school_name)
teacher.show()

print('--------------------------------------------------------------')

class Test:

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
print(Test.add(10, 20))
print(Test.multiply(10, 20))