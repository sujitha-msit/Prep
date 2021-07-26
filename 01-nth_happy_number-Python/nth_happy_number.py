# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)
import time
a=[]
def nth_happy_number(n):
	return a[n-1]
def ishappynumber(n):
	start_time=int(time.time())
	end_time=int(time.time())
	while(True):
		if (end_time-start_time<3):
			# print(start_time,end_time)
			li=map(int,list(str(n)))
			li=[x**2 for x in li]
			# print(li)
			if sum(li)==1:
				return True
			else:
				n=sum(li)
			end_time=int(time.time())
		else:
			return False
number=1
# n=int(input())
while(len(a)!=11):
	if ishappynumber(number):
		print("*****************************The numbber is************************",number)
		a.append(number)
	number+=1
# ishappynumber(1)
print(a)