a=10
b=20
c=30
print((a==b)&(a>b)&(b<c)|(c>a)&(a>b)|(b<c)&(b>a))
print((a==b)|(a>b)|(b<c)&(c>a)|(b<c)|(b>a))
print((a==b)|(a>b)|(b<c)&(c>a)&(b<c)|(b>a))