Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
\
>>> y = 7
>>> c = "please, I want {} sandwishes and {} donutes"
>>> print (c.replace("I", "We"))
please, We want {} sandwishes and {} donutes
>>> print(c.format(x ,y))
please, I want 5 sandwishes and 7 donutes
>>> print (c.upper("a"))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print (c.upper("a"))
TypeError: upper() takes no arguments (1 given)
>>> print (c.replace("a", "A"))
pleAse, I wAnt {} sAndwishes And {} donutes
>>> 
