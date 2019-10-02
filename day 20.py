Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = {}
>>> print(thisset)
{}
>>> thisset = {"apple", "banana", "cherry"}
>>> print(thisset)
{'apple', 'banana', 'cherry'}
>>> theset= {"ahmad", "ahmad", 1,2,1,5}
>>> print(theset)
{1, 2, 5, 'ahmad'}
>>> thisset= {"apple", "banana", "orange"}
>>> for x in thisset:
	print(x)

	
apple
banana
orange
>>> print("banana" in thisset)
True
>>> thisset.add("cherry")
>>> print(thisset)
{'cherry', 'apple', 'banana', 'orange'}
>>> thisset.update(["mango", "graps"])
>>> print(thisset)
{'cherry', 'mango', 'orange', 'apple', 'banana', 'graps'}
>>> 
