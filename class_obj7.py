class A:
    def sum(self,p,r,t):
        i=p*r*t
        return i
p=int(input("enter the value of p"))
r=int(input("enter the value of r"))
t=int(input("enter the value of t"))
obj=A()
i=obj.sum(p,r,t)
print("intrest is",i)