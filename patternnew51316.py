for i in range(1,5,1):
    for j in range(3,13+i,1):
        if(j<=6-i):
            print("-",end=" ")
        elif(j>=5-i and j<=5+i):
            print("*",end=" ")
        else:
            print("#",end=" ")
    print(" ")