Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = " hello, world"
>>> print(a.strip()) #return "hello, world"
hello, world
>>> a= "hello, world"
>>> a= "hello, world"len()
SyntaxError: invalid syntax
>>> a= "hello, world"
>>> print(len(a))
12
>>> a= "Hello, World"
>>> print(a.lower())
hello, world
>>> a= "Hello, World"
>>> print(a.upper())
HELLO, WORLD
>>> a= "hello, world"
>>> print(a.replace("H", "J"))
hello, world
>>> a= "Hello, World"
>>> print(a.replace("H","J"))
Jello, World
>>> a= "Hello, World"
>>> print(a.split(","))
['Hello', ' World']
>>> 
