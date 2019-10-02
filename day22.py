Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {}
>>> print(thisdict)
{}
>>> thisdict = {
	"brand": "ford",
	"model": "musting",
	"year": 1964
	}
>>> print (thisdict)
{'brand': 'ford', 'model': 'musting', 'year': 1964}
>>> x = thisdict["model"]
>>> print (x)
musting
>>> y= thisdict.get["year"]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    y= thisdict.get["year"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> y = thisdict.get("year")
>>> print(y)
1964
>>> thisdict["yera"] = 2018
>>> print (thisdict)
{'brand': 'ford', 'model': 'musting', 'year': 1964, 'yera': 2018}
>>> for x in thisdict:
	print(x)

	
brand
model
year
yera
>>>  for x in thisdict:
	 
SyntaxError: unexpected indent
>>> for x in thisdict:
	print(thisdict[x])

	
ford
musting
1964
2018
>>> for x in thisdict.values():
	print(x)

	
ford
musting
1964
2018
>>> print (thisdict.values())
dict_values(['ford', 'musting', 1964, 2018])
>>> for x,y in thisdict.item():
	print(x,y)

	
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    for x,y in thisdict.item():
AttributeError: 'dict' object has no attribute 'item'
>>> for x,y in thisdict.items():
	print(x,y)

	
brand ford
model musting
year 1964
yera 2018
>>> print (thisdict.items())
dict_items([('brand', 'ford'), ('model', 'musting'), ('year', 1964), ('yera', 2018)])
>>> 
