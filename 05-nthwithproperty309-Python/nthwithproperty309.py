# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	number=309
	i=0
	while(True):
		if property309(number):
			i=i+1
			print(number)
		if i==n:
			break
		number=number+1
	return number

def property309(number):
	for i in range(10):
		if str(i) not in str(number**5):
			return False
	return True

# number=309
# if "0" and "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" in str(number**5):

# 	print(True)
# else:
# 	print(False)
# print(property309(309
# ))
print(nthwithproperty309(1000))