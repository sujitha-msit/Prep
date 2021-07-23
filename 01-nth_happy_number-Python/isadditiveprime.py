def prime(number):
    if number<=2:
        return True
    if number%2==0:
        return False
    for i in range(3,int(number**0.5)+1,2):
        if number%i==0:
            return False
    return True
def isAdditivePrime(number):
    if prime(number):
        if(len(str(number))!=1):
            return isadditive(sum(map(int,list(str(number)))))
        else:
            return True
    else:
        print("not prime",number)
        return False
print(isAdditivePrime(31))
assert (isAdditivePrime(2) == True)
assert (isAdditivePrime(3) == True)
assert (isAdditivePrime(5) == True)
assert (isAdditivePrime(13) == False)
assert (isAdditivePrime(23) == True)
assert (isAdditivePrime(29) == True)
assert (isAdditivePrime(41) == True)
assert (isAdditivePrime(98) == False)
assert (isAdditivePrime(198) == False)
assert (isAdditivePrime(290) == False)
assert (isAdditivePrime(67) == True)
assert (isAdditivePrime(97) == False)
print("All test cases passed... :-)")