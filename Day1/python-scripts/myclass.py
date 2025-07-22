#!/usr/bin/python3

class MyClass:
    #Constructor - used for all initializations
    #self is equivalent to self reference/pointer in most languages
    #however, self is not a keyword
    def __init__(self, name):
        self.name = name

    # public method
    def sayHello(self):
        print(f"Hello, {self.name} !")
        self._method1()

    # protected method, can be inherited and invoked by child classes if any
    def _method1(self):
        print("This is a protected method")

    # private method, can't be accessed by child or from public scope
    def __method2(self):
        print("This is a private method")


obj = MyClass("Python")
obj.sayHello()
obj._method1()
obj.__method2()
