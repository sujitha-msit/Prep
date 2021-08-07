# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_prime(n):
	i=0
	number=2
	while(True):
		if ishappy(number) and isprime(number):
			i=i+1
			print(number)
		if i==n:
			break
		number=number+1
	return number
		

def ishappy(number):
	l=map(int,list(str(number)))
	l=map(square,l)
	if sum(l)==1:
		return True
	return False
def square(x):
	return x*x
def isprime(number):
	if number==2:
		return True
	if number%2==0:
		return False
	for i in range(3,int(number**0.5),2):
		if number%i==0:
			return False
	return True
print(ishappy(7))