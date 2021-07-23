def prime(number):
    if number<=2:
        return True
    if number%2==0:
        return False
    for i in range(3,int(number**0.5)+1,2):
        if number%i==0:
            return False
    return True
def isadditive(number):
    if prime(number):
        if(len(str(number))!=1):
            return isadditive(sum(map(int,list(str(number)))))
        else:
            return True
    else:
        print("not prime",number)
        return False
print(isadditive(31))