def core(n):
	if n % 3 == 0 and n % 5 == 0:
		return 'FizzBuzz'
	elif n % 3 == 0:
		return 'Fizz'
	elif n % 5 == 0:
		return 'Buzz'
	else:
		return n

def main():
	userInput = input('Inserisci un numero: ')
	try:
		userNumber = int(userInput)
		result = core(userNumber)
		print(result)
	except ValueError:
		print("L'input inserito non è un numero valido.")

if __name__ == "__main__":
	main()