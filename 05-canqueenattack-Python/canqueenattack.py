# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	x=qR
	y=qC
	a=[]
	while(0<x<8 and 0<y<8):
		a.append((x,y))
		x+=1
		y+=1
	x=qR
	y=qC
	while(0<x<8 and 0<y<8):
		a.append((x,y))
		x-=1
		y+=1
	x=qR
	y=qC
	while(0<x<8 and 0<y<8):
		a.append((x,y))
		x+=1
		y-=1
	x=qR
	y=qC
	while(0<x<8 and 0<y<8):
		a.append((x,y))
		x-=1
		y-=1
	if qR==oR or qC==oC:
		return True
	elif (oR,oC) in a:
		return True
	else:
		return False

	