# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	prev=0
	count=1
	for i in a:
		if i==prev:
			count+=1
		else:

	return newlist