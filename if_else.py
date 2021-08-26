a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter forth number"))
e=int(input("enter fifth number"))
if(a>b):
    if(a>c):
        if(a>d):
            if(a>e):
                print("a is greatest ",a)
            else:
                print("e is greates",e)
        else:
            if(d>e):
                print("d is greatest ",d)
            else:
                print("e is greatest ",e)
    else:
        if(c>d):
            if(c>e):
                print("c is greatest ",c)
            else:
                print("e is greatest ",e)
        else:
            if(d>e):
                print("d is greatest ",d)
            else:
                print("e is greatest ",e)
else:
    if(b>c):
        if(b>d):
            if(b>e):
                print("b is greatest ",b)
            else:
                print("e is greatest ",e)
        else:
            if(d>e):
                print(" d is greatest ",d)
            else:
                print("e is greatest",e)
    else:
        if(c>d):
            if(c>e):
                    print("c is greatest ",c)
            else:
                    print("e is greatest ",e)
        else:
            if(d>e):
                print("d is greatest ",d)
            else:
                print("e is greatest ",e)