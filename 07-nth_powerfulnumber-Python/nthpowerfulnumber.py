# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	number=1
	case=0
	a=[]
	while(len(a)==n):
		fac=primefactor(number)
		for i in fac:
			if number%(i**2)!=0:
				flag=False
				break
		if flag==True:
			a.append(number)
		
	return a[-1]		
		

def primefactor(num):
	a=[]
	for i in range(3,num//2+1):
		if num%i==0:
			if prime(i):
				a.append(i)
	return a

		


def prime(num):
	for i in range(3,int(num**0.5)):
		if num%i==0:
			return False
	return True
	