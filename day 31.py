Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_function():
	print("Hello from a function")

	
>>> my_function()
Hello from a function
>>> def my_function(fname):
	print(fname + "Refsenes")

	
>>> my_function("Emil")
EmilRefsenes
>>> my_function("Tobias")
TobiasRefsenes
>>> my_function("Linus")
LinusRefsenes
>>> def my_function(country = "norway"):
	print("I am from " + country)

	
>>> my_function("Sweden")
I am from Sweden
>>> my_function("India")
I am from India
>>> my_function()
I am from norway
>>> my_function("brazil")
I am from brazil
>>> 
