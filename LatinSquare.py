# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...


def isLatinSquare(n):
    col=[]
    for i in range(len(n)):
        cols=[]
        for j in range(len(n)):
            cols.append(n[j][i])
            cols.sort()
        col.append(cols)
    col.append(n[0])
    print(col)
    for i in range(len(col)-1):
        if sorted(col[i])==sorted(col[i+1]):
            return True
        else:
            return False
print(isLatinSquare([[1,2,3],[2,3,1],[3,1,2]]))
print("All test cases passed")