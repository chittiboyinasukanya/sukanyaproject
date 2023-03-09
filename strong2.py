import math
n=int(input("enter number"))
t=1
while t<n:
	dsum=0
	k=t
	while k>0:
		digit=k%10
		dsum=math.factorial(digit)+dsum
		k=k//10
	if t==dsum:
		print(t,end=" ")

	t=t+1
