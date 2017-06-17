def fizzBuzz():
    while True:
        print('Input an Interger')
        checkNum=input()
        rem=int(checkNum)%5
        rem1=int(checkNum)%3
        if rem==0 and rem1==0:
            print('Fizzbuzz')
        elif rem==0:
            print('Buzz')
        elif rem1==0:
            print('Fizz')
        else:
            print(checkNum)
        if rem==0 or rem1==0:
            break


fizzBuzz()
