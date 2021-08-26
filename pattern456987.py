for i in range(1,4,1):
    for j in range(1,4-i,1):
        print(" ",end="")
    for k in range(0,i*2-1,1):
        print("*",end="")
    print("")