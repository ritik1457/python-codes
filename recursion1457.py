def avr(n):
    if(n==1):
        return 1
    else:
        return n + avr(n-1)
print(avr(10))