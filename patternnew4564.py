for i in range(0,5,1):
    for j in range(1,10,1):
        if(j>i+1 and j<10-i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("*")