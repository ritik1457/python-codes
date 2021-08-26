for i in range(10,1,-1):
    for j in range(5,2*i-2,1):
        print("*",end=" ")
    for k in range(1,i-2,1):
        print(" ",end="")
    print(" ")