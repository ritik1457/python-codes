n=int(input("enter the number of student"))
i=0
for i in range (i,n,1):
    print("Enter student of ",i)
    hindi=int(input("enter the value of hindi"))
    english=int(input("enter the value of english"))
    punj=int(input("enter the value of punjabi"))
    total=hindi+english+punj
    print("total",total)
    per=total/3
    print("percentage",per)