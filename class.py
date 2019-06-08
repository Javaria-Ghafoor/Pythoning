"""
   in C++ you must have seen:
   int x;
   float y;
   string z;
   etc.
   the data types 'int', 'float', 'string' etc are like inbuilt classes
   moreover: A data type is a special kind of classifier, similar to a class. It differs
   from a class in that instances (here x, y, z) of a data type are identified only by their value.
   ..now what does that mean?
   LET'S SEE THROUGH EXAMPLES OF USER DEFINED CLASSES
"""


class Person:
    age = 20
    name = 'Bob'

    def display_age(self):
        return self.age

    def display_name(self):
        return self.name


"""
    Note that in the above mentioned example:
    1. self is an argument to the functions defined in the class.. it is a reference to objects that
       are made based on this class
    2. we just created a blueprint for objects of type "Person"
    3. the two functions display_age() and display_name =() are also termed as "methods" of the class
    4. this class has no user defined constructor
"""

#   creating a object p of class Person
p = Person()
#   using functions of class person for object p
print p.display_name(), 'has age', p.display_age()

"""
    Note that:
    to call a function of the class Person, we concatenated that function (without the parameter 'self')
    with a dot "." to the object
"""

#   another example


class Student:
    age = int()
    name = str()

    def __init__(self):
        # This is a user defined constructor. Whatever you code in this _init_ function would
        # run as soon as any object of type Student is constructed.
        self.age = 20
        self.name = 'Bob'
        # these^ are default values associated to parameters age and name of class Student once an object is constructed
        print 'user defined constructor called'
        # this line will be printed whenever this constructor function runs

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def display_age(self):
        return self.age

    def display_name(self):
        return self.name


"""
    Note that in the above example:
    1. we defined our own constructor which will overwrite the default constructor
    2. the parameters age and name of the functions set_age(age) and set_name(name)
       are not of the class Student since the parameters of the class Student are
       referenced by 'self'
"""

#   creating/constructing an object s of class Student
s1 = Student()
s2 = Student()
s3 = Student()

#dummy variables
name = str()
age = int()

#   using functions of class Student for objects s1 and s2
print 'Student 1:'
name = raw_input('Enter name: ')
age = raw_input('Enter age: ')
s1.set_name(name)
s1.set_age(age)
print 'Name: ', s1.display_name()
print 'Age: ', s1.display_age()
print 'Student 2:'
name = raw_input('Enter name: ')
age = raw_input('Enter age: ')
s2.set_name(name)
s2.set_age(age)
print 'Name: ', s2.display_name()
print 'Age: ', s2.display_age()
print 'Student 3:'
# let us not set any name and age and see what happens
print 'Name: ', s3.display_name()
print 'Age: ', s3.display_age()


"""
    Note that:
    to call a function of the class Student, we concatenated that function (skipping the parameter 'self')
    with a dot "." to the object
"""

"""
    Some terminologies:
    CLASS: A blueprint created by a programmer for an object. This defines a set of attributes
    that will characterize any object that is instantiated from this class
    OBJECT: An instance of a class. This is the realized version of the class, where the class
    is manifested in the program
    CONSTRUCTOR: A block of code executed on the construction of an object as soon as the
    compiler reads the line 
                             object=class_name()
    This block of code/ function is named as __init__ with a default parameter 'self'
"""

# for in depth analysis of different types of constructors.. refer to constructor.py
