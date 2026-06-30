import sys


if len(sys.argv) == 4:
	try:
		first_number = int(sys.argv[1])
		second_number = int(sys.argv[3])
	except ValueError:
		print("Error: Both arguments must be numbers")
		sys.exit(1)
	
	operator = sys.argv[2]
	
	if operator not in ["+", "-", "/", "*", "x"]:

		print("Unknown operator")
		sys.exit(1)
	if operator == "+":
		operation_r = first_number + second_number
		print(f"the solution is: {operation_r}")
	elif operator == "-":
		operation_r = first_number - second_number
		print(f"the solution is: {operation_r}")
	elif operator == "/":
		if second_number == 0:
			print("Error: Division by zero")
			sys.exit(1)
		operation_r = first_number / second_number
		print(f"the solution is: {operation_r}")
	elif operator == "*" or operator == "x":
		operation_r = first_number * second_number
		print(f"the solution is: {operation_r}")
else:
	print("Usage: calc.py <number> <operator> <number>")

