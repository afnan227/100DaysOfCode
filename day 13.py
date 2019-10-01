Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> S= []
>>> print(S)
[]
>>> numbers = [1,2,3,4,5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> thelist = ["apple", "banana", "cherry"]
>>> print(thelist)
['apple', 'banana', 'cherry']
>>> thelist = ["apple", "banana", "cherry", 1,2,3]
>>> print(thelist)
['apple', 'banana', 'cherry', 1, 2, 3]
>>> number= [1.2, 2.1, 3.7, 5.6]
>>> print(number)
[1.2, 2.1, 3.7, 5.6]
>>> thelist = ["apple", "banana", "cherry"]
>>> print(thelist[1])
banana
>>> for x in thelist:
	print(x)

	
apple
banana
cherry
>>> num= [1,2,3]
>>> for x in num:
	print(x)

	
1
2
3
>>> thelist = ["apple", "banana", "cherry"]
>>> thelist[1] = "blackcurrant"
>>> print(thelist)
['apple', 'blackcurrant', 'cherry']
>>> del thelist[0]
>>> print(thelist)
['blackcurrant', 'cherry']
>>> del thelist
>>> 
>>> listt= ["a", "b","c"]
>>> print (listt)
['a', 'b', 'c']
>>> del listt[0]
>>> print(listt)
['b', 'c']
>>> del listt[0]
>>> print(listt)
['c']
>>> 
