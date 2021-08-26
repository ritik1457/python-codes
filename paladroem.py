n=int(input("enter a number"))
m=n
sum=0
while(n>0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
if(sum==m):
    print("paledrome",+sum)
else:
    print("non")