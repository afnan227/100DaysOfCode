Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {
	"brand": "ford",
	"model": "musting",
	"year": 1998
	}
>>> mydict = thisdict.copy()
>>> print(mydict)
{'brand': 'ford', 'model': 'musting', 'year': 1998}
>>> mydict = dict (thisdict)
>>> print(mydict)
{'brand': 'ford', 'model': 'musting', 'year': 1998}
>>> 
 myfamily = {
	"child1":{
		"name":"email",
		"year":2004
		},
	"child2":{
		"name":"linus",
		"year": 2011
		}
	}
 
SyntaxError: unexpected indent
>>> myfamily = {
	"child1":{
		"name":"email",
		"year":2004
		},
	"child2":{
		"name":"linus",
		"year": 2011
		}
	}
>>> print(myfamily)
{'child1': {'name': 'email', 'year': 2004}, 'child2': {'name': 'linus', 'year': 2011}}
>>> thisdict = dict(brand="ford", model="musting", year= 1987)
>>> print(thisdict)
{'brand': 'ford', 'model': 'musting', 'year': 1987}
>>> 
