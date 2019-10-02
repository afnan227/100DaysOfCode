Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = {"apple", "banana", "cherry"}
>>> print (len(thisset))
3
>>> thisset.remove("banana")
>>> print(thisset)
{'cherry', 'apple'}
>>> thisset.discard("apple")
>>> print(thisset)
{'cherry'}
>>> thisset= {"apple", "banana", "cherry"}
>>> x = thisset.pop()
>>> print(x)
cherry
>>> print(thisset)
{'apple', 'banana'}
>>> thisset.clear()
>>> print(thisset)
set()
>>> thisset = {"apple", "banana", "cherry"}
>>> del thisset
>>> print (thisset)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (thisset)
NameError: name 'thisset' is not defined
>>> thisset = set (("ahmad", "hasan", "naif"))
>>> print (thisset)
{'naif', 'hasan', 'ahmad'}
>>> 
