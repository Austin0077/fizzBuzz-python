# This program says hello and asks for my name.

print('Hello World!')
print('What is Your Name?')#as for their name
myName = input()
print('it is Good to meetyou, ' + myName)
print('the length of your name is:')
print(len(myName))
print('What is Your age?')# ask for their age
myAge = input()
print('You will be ' +str(int(myAge) + 1) + ' in a year.')
print('Enter an Interger')
#nt(s)=input()
s=input()
print(int(s))
if myName=='Austin':
	print('You Have Such a Nice Name,'+myName)
else:
	print("Si Ungeitwa Jina Ingine")
if int(s)<9:
	print('Nice Choice of Interger')
else:
	print('Chagua vitu Ndogo haitabadilishwa kuwa food')
if myName=='Austin':
	print('Welcome,')
elif int(myAge)>5:
	print('You"re not Austin, So we Ni?')
else:
	print('Good Bye Hacker')