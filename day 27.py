Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= 33
>>> b= 200
>>> if b > a:
	print("b is greater than a")

	
b is greater than a
>>> if b > a:
print("b is greater than a")
SyntaxError: expected an indented block
>>> a= 33
>>> b= 33
>>> if b > a:
	print("b is greater than a")
	elif a == b:
		
SyntaxError: invalid syntax
>>> if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")

	
a and b are equal
>>> a = 200
>>> b = 33
>>> if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")

	
a is greater than b
>>> a = 200
>>> b = 33
>>>  if b > a:
	print("b is greater than a")
	
SyntaxError: unexpected indent
>>> if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a")

	
b is not greater than a
>>> a = 200
>>> b = 33
>>> if a > b: print("a is greater than b")

a is greater than b
>>> a =2
>>> b = 330
>>> print("A") if a > b else print ("B")
B
>>> a = 330
>>> b = 330
>>> print("A") if a > b else print("=") if a == b else print("B")
=
>>> 
>>> a = 200
>>> b = 33
>>> c= 500
>>> if a > b and c > a:
	print("both condition are true ")

	
both condition are true 
>>> a = 200
>>> b = 33
>>> c= 500
>>> if a > b or a > c:
	print("At least one of the condition is true")

	
At least one of the condition is true
>>> x = 41
>>> if x > 10:
	print("above ten,")
if x > 20:
	
SyntaxError: invalid syntax
>>> f x > 10:
	print("above ten,")
	
SyntaxError: invalid syntax
>>> if x > 10:
	print("above ten,")
	if x > 20:
		print("and also above 20!")
		else:
			
SyntaxError: invalid syntax
>>> if x > 10:
	print("above ten,")
	if x > 20:
		print("and also above 20!")
	else:
		print("but not abve 20.")

		
above ten,
and also above 20!
>>> 
