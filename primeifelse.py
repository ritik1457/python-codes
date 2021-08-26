n=10
i=1
j=1
while(i<=n):
    j=2
    while(j<i):
        if(i%j==0):
            break
        j=j+1
    if(j==i):
        print("prime no",j)      
    i=i+1
  