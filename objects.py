'''OBJECTS
    (1) What is object
    (2) Iterable objects & Range
    (3) Dictionary
    (4) Error handling system
'''

import array  # package / module
import math
from math import ceil, asin

print('=============What is object?============')
# An object has state and method properties.
# Everything is object in Python

print(type('Hello world!'))
print(type(111))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritance | Polymorphism
result1 = math.ceil(97.7)
print("result math ceil1", result1)

result1 = math.ceil(98.7)
print("result math ceil2", result1)
