class MyClass:
    class_var = 10

    def __init__(self, my_state):
        self.my_state = my_state

    def my_instance_method(self):
        print("In my instance method ", self.my_state)

    @classmethod
    def my_class_method(cls, a):
        print("In my class method", cls.class_var, " with parameter ", a) #, cls.my_state)

    @staticmethod
    def my_static_method(b):
        print("In my static method with param ", b)

if __name__ == "__main__":
    my_cls = MyClass("NY")
    my_cls.my_instance_method()
    my_cls.my_class_method(10)
    my_cls.my_static_method(21)

    MyClass.my_class_method(20)
    MyClass.my_static_method(200)