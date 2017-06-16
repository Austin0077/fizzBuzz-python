def fizzBuzz():
	checkNum=0

	while checkNum!=5 and checkNum!=3:
		print('Input an Interger')
		checkNum=input()
		if int(checkNum)%5==0 and int(checkNum)%3==0:
			print('Fizzbuzz')
		elif int(checkNum)%5==0:
			print('Buzz')
		elif int(checkNum)%3==0:
			print('Fizz')
		else:
			print(checkNum)

fizzBuzz()