Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = {1,3,5,7,8}
>>> thisset.update([4,8,12])
>>> print(thisset)
{1, 3, 4, 5, 7, 8, 12}
>>> thisset.remove(8)
>>> print(thisset)
{1, 3, 4, 5, 7, 12}
>>> thisset.clear()
>>> print(thisset)
set()
>>> thisdict= {
	"name": "pigeon",
	"type": "bird",
	"skin cover": "feathers"
	}
>>> x = thisdict["type"]
>>> print(x)
bird
>>> thisdict["skin cover"]= "leather"
>>> print (thisdict)
{'name': 'pigeon', 'type': 'bird', 'skin cover': 'leather'}
>>> 
