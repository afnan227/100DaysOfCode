Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_function(food):
	for x in food:
		print(x)

		
>>> fruits = ["apple", "banana", "cherry"]
>>> my_function(fruits)
apple
banana
cherry
>>> def my_function(x):
	return 5 * x

>>> print(my_function(3))
15
>>> print(my_function(5))
25
>>>  print(my_function(9))
 
SyntaxError: unexpected indent
>>> print(my_function(9))
45
>>> def my_function(child3, child2, child1):
	print("the youngest child is " + child3)

	
>>> my_function(child1 = "Emil", child2= "tobias", child3= "linus")
the youngest child is linus
>>> def my_function(*kids):
	print("the youngest child is " + kids[2])

	
>>> my_function("Emil", "TObias", "Linus")
the youngest child is Linus
>>> def tri_recursion(k):
		if(k>0):
		result = k+tri_recursion(k-1)
		
SyntaxError: expected an indented block
>>> def tri_recursion(k):
		if(k>0):
			result = k+tri_recursion(k-1)
			print(result)
		else:
			result = 0
			return result
		print("\n\nRecursion Example Results")

		
>>> tri_recursion(6)
1


Recursion Example Results
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tri_recursion(6)
  File "<pyshell#31>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  File "<pyshell#31>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  File "<pyshell#31>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  [Previous line repeated 2 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> 
