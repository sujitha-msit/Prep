# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def fun_nth_smithnumber(n):
   
    number=4
    i=0
    while(True):
        if smith(number)==True:
            i+=1
        if i==n:
            break
        number=number+1
    return number
def smith(number):
    a=[]
    original=number
    for i in range(2,(number//2)+1):
        if number%i==0:    
            if prime(i):
                
                a.append(i)
    count=0
    # print(a)
    for i in a:
        while(number%i==0):
            number=number//i
            if len(str(i))>1:
                temp=sum(map(int,list(str(i))))
                count+=temp
            else:
                count+=i
    if sum(map(int,list(str(original))))==count:
        return True
    else:
        return False
def prime(number):
    if number==2:
        return True
    if number%2==0:
        return False
    for i in range(3,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
# print(smith(22))
for i in range(5):
    print(fun_nth_smithnumber(i))
