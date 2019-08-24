Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x =5
>>> y="jhon"
>>> print(x)
5
>>> print(y)
jhon
>>> x=4 #x is of type int
>>> x= "Sally" # x is now of type str
>>> print(x)
Sally
>>> x="jhon"
>>> print(x)
jhon
>>> x='jhon'
>>> print(x)
jhon
>>> x,y,z ="Orange","Banan","Cheery"
>>> print(x)
Orange
>>> print(y)
Banan
>>> print(z)
Cheery
>>> x=y=z= "orange"
>>> print(x)
orange
>>> print(y)
orange
>>> print(z)
orange
>>> x= "awesome"
>>> print("python is " + x)
python is awesome
>>> x= "python is"
>>> y="awesome"
>>> z= x+y
>>> print(z)
python isawesome
>>> x= 5
>>> y="jhon"
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
