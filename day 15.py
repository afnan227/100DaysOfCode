Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thelist = ["apple", "banana", "cherry"]
>>> print(len(thelist))
3
>>> thelist.append("orange")
>>> print(thelist)
['apple', 'banana', 'cherry', 'orange']
>>> thelist.insert(1, "berry")
>>> print(thelist)
['apple', 'berry', 'banana', 'cherry', 'orange']
>>> thelist.remove("banana")
>>> print(thelist)
['apple', 'berry', 'cherry', 'orange']
>>> thelist.pop()
'orange'
>>> print(thelist)
['apple', 'berry', 'cherry']
>>> thelist.clear()
>>> print(thelist)
[]
>>> thelist = ["apple", "banana", "cherry"]
>>> mylist= thelist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> listt= ["ahmad", "omar", "khalid"]
>>> mylist = listt.copy()
>>> listt.pop(0)
'ahmad'
>>> print(mylist)
['ahmad', 'omar', 'khalid']
>>> print(listt)
['omar', 'khalid']
>>> mylist = listt
>>> listt.pop(0)
'omar'
>>> print(mylist)
['khalid']
>>> print(listt)
['khalid']
>>> thelist = ["apple", "banana", "cherry"]
>>> mylist = list(thelist)
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist = list(("ahmed", "omar", "khalid"))
>>> print(thislist)
['ahmed', 'omar', 'khalid']
>>> 
