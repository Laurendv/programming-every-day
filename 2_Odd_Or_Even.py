num = int(input('What is the number?'))
check = int(input('What is the number?'))
if num % check == 0 :
	print('Check divides evenly.')
elif num % 2 == 0 and num % 4 != 0 : 
	print('Your number is even.')
elif num % 4 == 0 :
	print('Your number is a multiple of 4.')
else :
	print('Your number is odd.')
