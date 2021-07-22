# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	number=1
	case=0
	a=[]
	if n==0:
		return 1
	while(len(a)!=n):
		print("The number here is ",number)
		flag=True
		fac=primefactor(number)
		print("The prime factors for the number is",fac)
		if len(fac)>1:
			for i in fac:
				if number%(i)!=0:
					flag=False
					break
		else:
			print("for thiose it it flag is false",number)
			flag=False
		
		if flag==True:
			a.append(number)
		number+=1
			
	print("the powerfulnumbers are ",a)	
	return a[-1]	
		

def primefactor(num):
	a=[1]
	for i in range(2,num//2+1):
		if num%i==0:
			if prime(i):
				a.append(i)
				a.append(i**2)
	return a

		


def prime(num):
	if num<=2:
		return True
	if num%2==0:
		return False
	for i in range(3,int(num**0.5)+1,2):
		if num%i==0:
			return False
	return True
# print(primefactor(6))
print(nthpowerfulnumber(10)	)