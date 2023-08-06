number = int(input('enter your number:'));
check  = False
for i in range(2, number-1):
	if(number%i==0):
		print("morakab")
		check = True
		break
if (not check):
	print("aval")
	

