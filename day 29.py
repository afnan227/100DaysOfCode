Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ["apple", "banana", "cherry"]
>>> for x in fruits:
	print(x)

	
apple
banana
cherry
>>> for x in "banana":
	print(x)

	
b
a
n
a
n
a
>>> for x in fruits:
	print(x)
	if x == "banana"
	
SyntaxError: invalid syntax
>>> for x in fruits:
	print(x)
	if x == "banana":
		break

	
apple
banana
>>> for x in fruits:
	if x == "banana":
		break
	print(x)

	
apple
>>> for x in fruits:
	if x == "banana":
		continue
	print(x)

	
apple
cherry
>>> 
