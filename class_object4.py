class A:
    def sum(self,a,b):
        c=a+b
        return c
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
obj=A()
c=obj.sum(a,b)
print("sum is ",c)
