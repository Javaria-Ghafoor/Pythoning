"""The Heron of Alexandria Algorithm is a method to find the approximate
 square root of a number. The basic idea is that if y is an overestimate
 to the square root of a non-negative real number x then x/y will be an
 underestimate, or vice versa, and so the average of these two numbers
 may reasonably be expected to provide a better approximation"""

import random

x = float(int(raw_input("Enter a positive integer to find square root: ")))
y = random.randint(1, x)   #the square root of an int must lie between 1 and that int
while not x-0.0001 < y*y < x+0.0001:   #more narrow the range, more better the approximation
        y = (y + x/y)/2
print 'The square root using Heron of Alexandria Algorithm is: ', y
print '..well, that\'s a good approximation :P..'
