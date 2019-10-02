Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist= ["nourah", "ameera","afnan", "nada"]
>>> thislist.append("hessa")
>>> print(thislist)
['nourah', 'ameera', 'afnan', 'nada', 'hessa']
>>> thislist.insert(2, "yasmeen")
>>> print(thislist)
['nourah', 'ameera', 'yasmeen', 'afnan', 'nada', 'hessa']
>>> thislist.remove("hessa")
>>> print(thislist)
['nourah', 'ameera', 'yasmeen', 'afnan', 'nada']
>>> thislist.pop()
'nada'
>>> print(thislist)
['nourah', 'ameera', 'yasmeen', 'afnan']
>>> mylist= thislist.copy()
>>> print(mylist)
['nourah', 'ameera', 'yasmeen', 'afnan']
>>> print(thislist[3])
afnan
>>> thislist[1]= "saba"
>>> print(thislist)
['nourah', 'saba', 'yasmeen', 'afnan']
>>> print(len(thislist))
4
>>> thislist.clear()
>>> print(thislist)
[]
>>> tuple=("java","python","swift" )
>>> if "python" in tuple:
	print("Yes, 'python' is in tuple")

	
Yes, 'python' is in tuple
>>> 
