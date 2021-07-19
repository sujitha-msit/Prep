# removeRowAndCol (non-destructive and destructive)
# Here we will write removeRowAndCol(row, col), 
# Do not use copy.deepcopy and directly construct 
# the modified 2d list.

# The function takes a rectangular list L and two ints, 
# row and col. the goal is to obtain a version of the list 
# that has the given row and given column removed. 
# You may assume that row and col are both legal values 
# (that is, they are non-negative integers that are smaller 
# than the largest row and column, respectively). For example, 
# the list shown to the left would lead to the result shown on 
# the right when called with row 1 and column 2.

# list
# [ [ 2, 3, 4, 5],
#   [ 8, 7, 6, 5],
#   [ 0, 1, 2, 3] ]

# result
# [ [ 2, 3, 5],
#   [ 0, 1, 3] ]
# Destructive way of doing it
def removeRowAndCol(L, row, col):
    L.pop(row)
    for i in range(len(L)):
        L[i].pop(col)
    return L
def nondest(L,row,col):
    res=[]
    for i in range(len(L)):
        a=[]
        if i!=row:
            # print(i)
            for j in range(len(L[i])):
                if j!=col:
                    # print(j)
                    a.append(L[i][j])

            res.append(a)
    return res


lis=[ [ 2, 3, 4, 5],
  [ 8, 7, 6, 5],
  [ 0, 1, 2, 3] ]
# print(removeRowAndCol(lis,1,2))
print("This is non desturctive method of doing it",nondest(lis,1,2))

# Write your own test cases.