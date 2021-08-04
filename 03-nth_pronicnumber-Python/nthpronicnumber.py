# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
	return a[n]
a=[]
i=0
while(len(a)!=51):
	a.append(i*(i+1))
	i=i+1