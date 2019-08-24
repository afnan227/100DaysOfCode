Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=1
>>> y=2.8
>>> z=1j
>>> print(type(x))
<class 'int'>
>>>  print(type(y))
 
SyntaxError: unexpected indent
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> x=1
>>> y=345566
>>> z=-34567
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> x=1.10
>>> y=1.0
>>> z=-34.88
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x=35e3
>>> y=12E4
>>> z=-98E7e100
SyntaxError: invalid syntax
>>> z=-98.7e100
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x=3+5j
>>> y=5j
>>> z=-5j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>> print(type(z))
<class 'complex'>
>>> x=1
>>> y=2.8
>>> z=1j
>>> a=float(x)
>>> b=int(y)
>>> c=complex(x)
>>> print(x)
1
>>> print(a)
1.0
>>> print(b)
2
>>> print(c)
(1+0j)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> import random
>>> print(random.randrange(1,10))
7
>>> 
>>> print(random.randrange(1,10))
7
>>> print(random.randrange(1,10))
7
>>> print(random.randrange(1,10))
5
>>> print(random.randrange(1,10))
2
>>> print(random.randrange(1,10))
2
>>> print(random.randrange(1,10))
7
>>> 
