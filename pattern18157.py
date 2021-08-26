for i in range(0,6,1):
    for j in range(1,6,1):
        if(j==i or j==6-i):
            print("*",end="")
        else:
            print(" ",end="")
    print("")