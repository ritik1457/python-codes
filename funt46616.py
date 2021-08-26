def SI(p,r,t):
    si=p*r*t
    return si
p=int(input("enter value of principle"))
r=int(input("enter value of rate of intrest"))
t=int(input("enter value of time"))
si=SI(p,r,t)
print("value of SI",si)