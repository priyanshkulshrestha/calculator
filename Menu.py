choice = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division :")
a = input("enter the first number:")
b = input("enter the second number:")
if choice == "1":
	import add as a1
	a1.add(a, b)
if choice == "2":
	import sub as s1
	s1.sub(a, b)
if choice == "3":
	import multiply as m1
	m1.mul(a, b)
if choice == "4":
	import division as d1
	d1.div(a, b)
