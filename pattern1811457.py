n = int(input(""))
for i in range(1,n,1):
    if(n%i==0):
        break
if(i==n):
    print("prime",n)
else:
    print("no prime")