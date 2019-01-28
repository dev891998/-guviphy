num=int(input())
if n<=1000:
	for i in range(2,num//2):
		if (num%i)==0:
			print(num, "is not a prime number")
			else:
				print(num, "is a prime number")
