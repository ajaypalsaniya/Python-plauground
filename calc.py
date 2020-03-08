print("====WELCOME IN YOUR CALC====")

while True:
	choice = input("Enter your choice do you want to calculate (y/n):")
	
	if choice == "y":

		n1 = float(input("Enter your first number:"))
		operation = str(input("What operation do you want?:"))
		n2 = float(input("Enter your second number:"))

		if operation == "+":
			print(f"addition of numbers is:",n1+n2)
		elif operation == "-":
			print(f"subtraction of numbers is:",n1-n2)
		elif operation == "*":
			print(f"multiplication of numbers is:",n1*n2)
		elif operation == "/":
			print(f"division of numbers is:",n1/n2)
		else:
			print("Invalid input")
	else:
		break