Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {
	"barnd": "ford",
	"model": "musting",
	"year": 1964
	}
>>> if "model" in thisdict:
	print ("Yes, 'model' is one of the keys")

	
Yes, 'model' is one of the keys
>>> print (len(thisdict))
3
>>> thisdict["color"]= "red"
>>> print (thisdict)
{'barnd': 'ford', 'model': 'musting', 'year': 1964, 'color': 'red'}
>>> thisdict.pop("model")
'musting'
>>> print (thisdict)
{'barnd': 'ford', 'year': 1964, 'color': 'red'}
>>> thisdict.popitem()
('color', 'red')
>>> print (thisdict)
{'barnd': 'ford', 'year': 1964}
>>> del thisdict["model"]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    del thisdict["model"]
KeyError: 'model'
>>> thisdict.clear()
>>> print (thisdict)
{}
>>> 
