for i in range(0,5,1):
    for j in range(1,13,1):
        if(j>2*i-1 and j<=13-2*i):
            print(" ",end="")
        else:
            print("*",end="")
    print("")