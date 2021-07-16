# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def trianglearea(s1, s2, s3):
	s=(s2+s1+s3)/3
	area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
	if area>0:
		return area
	else:
		return 0
	

def fun_nearestbusstop(street):
	if street%8<=4:
		return street - (street%8)
	else:
		return street +(8- (street % 8))
# print(fun_nearestbusstop(12))