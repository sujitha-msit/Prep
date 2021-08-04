def pow(num,power):
    if power==0:
        return 1
    else:
        return num*pow(num,power-1)
print(pow(2,3))
