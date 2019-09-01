Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> age= 36
>>> txt="my name is jhon, I am " + age
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    txt="my name is jhon, I am " + age
TypeError: can only concatenate str (not "int") to str
>>> print(txt)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(txt)
NameError: name 'txt' is not defined
>>> age =36
>>> txt="my name is jhon, I am "
>>> txt="my name is jhon, I am {} "
>>> print(txt.format(age))
my name is jhon, I am 36 
>>> quantity =3
>>> itemno = 567
>>> price = 49.95
>>> myorder = " I want {} pieces of item {} for {} dollars. "
>>> print (myorder.format(quantity,itemno,price ))
 I want 3 pieces of item 567 for 49.95 dollars. 
>>> quantity =3
>>> itemno = 567
>>> price = 49.95
>>> myorder = " I want pay {2}dollars for {0} pieces of item {1}. "
>>> print(myorder.format(quantity,itemno, price))
 I want pay 49.95dollars for 3 pieces of item 567. 
>>> 
