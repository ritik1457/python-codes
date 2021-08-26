for i in range(0,7,1):
    for j in range(1,15,1):
        if(j>8-i and j<8+i):
            print(" ",end="")
        else:
            print("*",end="")
    print("")        