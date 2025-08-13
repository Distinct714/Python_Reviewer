# CLASS METHOD

# classmethod() function is used to define a method that is bound to the class and not the instance of the class. 
# This means that it can be called on the class itself rather than on instances of the class.

class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Create an instance of MyClass
obj = MyClass(10)

# Call the get_value method on the instance
print(obj.get_value())


# The classmethod() is an inbuilt function in Python, which returns a class method for a given function. 
# This means that classmethod() is a built-in Python function that transforms a regular method into a class method. 
# When a method is defined using the @classmethod decorator (which internally calls classmethod()), 
# the method is bound to the class and not to an instance of the class. 
# As a result, the method receives the class (cls) as its first argument, rather than an instance (self).

class Student:

    name = "Joshua"

    def print_name(obj):
        print("The name of this person is: ", obj.name)

# create print_name classmethod before creating this line print_name().
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()


# ANOTHER SAMPLE

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

#
class Course:
    course = 'IT'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Course.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to PUP for Nothing!"

# Creating instances
g1 = Course("Joshua")
g2 = Course("Gerald")

# Calling class methods
print(Course.get_course())  
print(Course.get_instance_count())  

# Calling static method
print(Course.welcome_message())  



