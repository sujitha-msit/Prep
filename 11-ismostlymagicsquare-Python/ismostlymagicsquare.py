# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

from typing_extensions import ParamSpecArgs


def ismostlymagicsquare(a):
	# Your code goes here
	r=[]
	
	diag=0
	prev=sum(a[0][:])
	for i in range(len(a)):
		row_sum=0
		col_sum=0
		for j in range(len(a)):
			row_sum+=a[i][j]
			col_sum+=a[j][i]
			if i==j:
				diag+=a[i][j]
		if row_sum==prev and row_sum==col_sum:
			pass
		else:
			return False
	if row_sum==diag:
		return True
	else:
		return False

	# 	r.(row_sum)
	# 	r.append(col_sum)
	# r.append(diag)
	# if row_sum==col_sum and col_sum==diag and diag==row_sum:
	# 	return True
	# else:
	# 	return False
	# if  len(set(r))==1:
	# 	return True
	# else:
# 	# 	return False
# a=[[1, 7, 6], [9, 5, 1], [4, 3, 8]]
# print(ismostlymagicsquare(a))
