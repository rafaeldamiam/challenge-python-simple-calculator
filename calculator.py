def ask_number():
	number = input('Enter the number: ')
	return number
	pass

def ask_operator():
	operator = input('Enter the operator (+, -, x, /): ')
	return operator
	pass

def addition(n1, n2):
	plus = n1 + n2
	return plus
	pass

def subtraction(n1, n2):
	minus = n1 - n2
	return minus
	pass

def multiplication(n1, n2):
	times = n1 * n2
	return times
	pass

def division(n1, n2):
	divide = n1 * n2
	return divide
	pass


number_one = float(ask_number())
operator = ask_operator()
number_two = float(ask_number())
result = " "

match operator:
	case "+":
		result = addition(number_one, number_two)
	case "-":
		result = subtraction(number_one, number_two)
	case "x":
		result = multiplication(number_one, number_two)
	case "/":
		result = division(number_one, number_two)
	case _:
		print("Enter a correct operator")
		os._exit(1)

print(f'The result is: {number_one} {operator} {number_two} = {result}')