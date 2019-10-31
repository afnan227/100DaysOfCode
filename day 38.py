Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> cars = ["Ford", "Volo", "BMW"]
>>> for x in cars
SyntaxError: invalid syntax
>>> for x in cars:
	print (x)

	
Ford
Volo
BMW
>>> car = ["Ford", "Volvo", "BMW"]
>>> car.append("Honda")
>>> print(car)
['Ford', 'Volvo', 'BMW', 'Honda']
>>> car.pop(1)
'Volvo'
>>> print (car)
['Ford', 'BMW', 'Honda']
>>> car.remove("Honda")
>>> print(car)
['Ford', 'BMW']
>>> 
