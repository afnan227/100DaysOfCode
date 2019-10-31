Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def tri_recursion(k):
	if(k>0):
		result = k+tri_recursion(k-1)
		print(result)
	else:
		result = 0
	return result

>>> print ("\n\nRecursion Example Results")


Recursion Example Results
>>> tri_recursion(5)
1
3
6
10
15
15
>>> 
