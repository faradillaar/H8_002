#INTEGER
print(123123123123123123123123123123123123123123123123 + 1)
print(10)
print(type(10))

#Floating-Point Numbers
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

#String
print("Hacktiv8")
print(type("Hacktiv8"))
print('')
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')

#Boolean Type, Boolean Context, and "Truthiness"
print(type(True))
print(type(False))

#Variable Assignment
n = 300
print(n)
n
n = 1000
print(n)
n
a = b = c = 300
print(a, b, c)

#Variable Types in Python
var = 23.5
print(var)
var = "Now I'm a string"
print(var)

#Variable Names
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)
_kepala_naga = True
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)

#Operators and Expressions in Python
a = 10
b = 20
a + b

a = 10
b = 20
a + b - 5

#Arithmetic Operators
a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

10 / 5

#Comparison Operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

a = 30
b = 30
print(a == b)
print(a <= b)
print(a >= b)

#String Manipulation
# + Operators
s = 'foo'
t = 'bar'
u = 'baz'
print(s + t)
print(s + t + u)
print('Hacktiv8 ' + 'PTP')
# * Operators
s = 'foo.'
s * 4
# in Operators
s = 'foo'
print(s in 'That food for us')
print(s in 'That good for us')
# Case Conversion
s = 'HackTIV8'
# Capitalize
print(s.capitalize())
# Lower
print(s.lower())
# Swapcase
print(s.swapcase())
# Title
print(s.title())
# Uppercase
print(s.upper())

#Python List
a = ['foo', 'bar', 'baz', 'qux']
print(a)

#List Are Ordered
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']
a == b

#List can Contain Arbitary Objects
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)

#List Elements can be Accessed by Index
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])
print(a[5])
print(a[-1])
print(a[-6])
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:5]
# The concatenation (+) and replication (*) operators:
print(a)
print(a + ['grault', 'garply'])
print(a * 2)
# len(), min(), max()
print(a)
print(len(a))
print(min(a))
print(max(a))

#Modifying a Single List Values
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
a[2] = 10
a[-1] = 20
print(a)
# A list item can be deleted with the del command:
del a[3]
print(a)

#Modifying Multiple List Value
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)