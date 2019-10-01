Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thistuple = ("apple", "banana", "cherry")
>>> print (thistuple)
('apple', 'banana', 'cherry')
>>> thetuple = ()
>>> print(thetuple)
()
>>> thetuples = (3,)
>>> print (thetuples)
(3,)
>>> thetuplees = (1,3.3, 4.1, 9)
>>> print(thetuplees)
(1, 3.3, 4.1, 9)
>>> thituple = ("ahmad", 1.1, 4, " بايثون")
>>> print(thituple)
('ahmad', 1.1, 4, ' بايثون')
>>> thtuple = ("apple", "banana", "cherry")
>>> print (thtuple[1])
banana
>>> for x in thtuple:
	print(x)

	
apple
banana
cherry
>>> thtuple[3]= "orange"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    thtuple[3]= "orange"
TypeError: 'tuple' object does not support item assignment
>>> thtuple = ("apple", "banana", "cherry")
>>> thtuple [3]= "orange"
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    thtuple [3]= "orange"
TypeError: 'tuple' object does not support item assignment
>>> thisstuple = ("apple", "banana", "cherry")
>>> thisstuple[3] = "orange"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    thisstuple[3] = "orange"
TypeError: 'tuple' object does not support item assignment
>>> del thisstuple
>>> print (thisstuple)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print (thisstuple)
NameError: name 'thisstuple' is not defined
>>> print (thisstuple [0:2)
       
SyntaxError: invalid syntax
>>> thisstuple = ("apple", "banana", "cherry")
>>>  print (thisstuple [0:2])
 
SyntaxError: unexpected indent
>>> print (thisstuple [0:2])
('apple', 'banana')
>>> 
