# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):

	length=len(str(n))
	div=10**(length-k-1)
	first=n/div
	last=n%div
	first=(first//10)*10+d
	number=first*div+last
	print(int(number))


