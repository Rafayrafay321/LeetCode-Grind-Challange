# defining the class in python
class Test:    # The class object is created when the class is defined
    x = 5
    # creating the init function to create access the object (It is like constructor)
    # Init function must contain the one "Self" arrgument 

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    # There are usually three types of functions in python
    # Numnber 1: Object / Instance method

    def show(self):     # It is also take self or 0ne atrribute always
        print(self.a,self.b)

    # defining the class method whic is used to acces class attributes

    @classmethod
    def f1(cls):
        print(cls.x)
    

    # Static Method
    @staticmethod
    def f2():
        print("Static method")

# Definig the instance objec

t1 = Test(7,6)  # Thid is the class object
t2 = Test(9,7)

# Calling the Instance method
t1.show()
t2.show()

# Calling the Class method using the class name

Test.f1()

# Calling the static method
# It can called by both objects class as well as the innstance object
t1.f2()
Test.f2()