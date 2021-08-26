for i in range(1,7,1):
    for j in range(7,1,-1):
        if(j==i):
            print("*",end="")
        else:
            print(" ",end="")
    print("")