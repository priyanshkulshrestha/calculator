choice = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication,4 for division,and 5 for modulo :")
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
if choice == "1":
	import addition as a1
	a1.add(a, b)
if choice == "2":
	import subtraction as s1
	s1.sub(a, b)
if choice == "3":
	import multiplication_fucntion as m1
	m1.mul(a, b)
if choice == "4":
	import Division as d1
	d1.div(a, b)
if choice == "5":
	import modulus as m2
	m2.mod(a, b)
	
