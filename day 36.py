Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfunc(n):
	return lambda a : a * n
mydoubler = myfunc(2)
SyntaxError: invalid syntax
>>> def myfunc(n):
	return lambda a : a * n

>>> mydoubler = myfunc(2)
>>> print(mydoubler(11))
22
>>> def myfunc(n):
	return lambda a : a * n

>>> mytripler = myfunc(3)
>>> print (mytripler(11))
33
>>> def myfunc(n):
	return lambda a : a * n

>>> mydoubler = myfunc(2)
>>> mytripler = myfunc(3)
>>> print(mydoubler(11))
22
>>> print(mytripler(11))
33
>>> 
