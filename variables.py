"""
    We can use the type() function to know which class a variable or a value belongs to
    and the isinstance() function to check if an object belongs to a particular class.
"""
"""
   What is a class?
   in C++ you must have seen:
   int x;
   float y;
   string z;
   etc.
   the data types 'int', 'float', 'string' etc are like inbuilt classes
   moreover: A data type is a special kind of classifier, similar to a class. It differs
   from a class in that instances (here x, y, z) of a data type are identified only by their value.
   ..now what does that mean?
   for detail refer to class.py after referring to function.py
"""
#   In python, you can declare/initialize a variable without mentioning its data type
a = 4
b = 2.0
c = 2 + 7j
d = 'hello'
#   use of type() function
print a, ' belongs to ', type(a)
print b, ' belongs to ', type(b)
print c, ' belongs to ', type(c)
print d, ' belongs to ', type(d)
#   use of isinstance() function
print c, 'is a complex number?: ', isinstance(c, complex)
print d, 'is a complex number?: ', isinstance(d, complex)

"""
    Now, since int, float, complex etc are inbuilt classes, therefore they have an
    inbuilt constructor.
    for "what is a constructor?" refer to class.py
    in C++:
    int x;
    this line when read by the compiler calls the inbuilt constructor of "int" class
    and an instance (object) x is constructed
    in python:
    to construct an instance of a certain class class_name (say) you do the following:
    object = class_name()
"""

#   how we declare a certain data type in python

x = int()
y = float()
z = complex()

#inputting variables.. Python 3,7 uses input() while Pyhton2.7 uses raw_input()

x = raw_input('Enter an integer: ')
y = raw_input('Enter a floating point number: ')
z = raw_input('Enter a complex number: ')

print 'x = ', x
print 'y = ', y
print 'z = ', z
