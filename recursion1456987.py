def prime(n,i):
    if(i<n):
        if(n%i==0):

            print("n is prime number")
            exit
        else:
            prime(n,i+1)
print(prime(3,2))