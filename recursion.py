def tab(n,i):
    if(i==10):
       exit
    else:
        print(n,"*",i,"=",n*i)
        i=i+1
        tab(n,i)
tab(2,1)