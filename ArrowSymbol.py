n=int(input())

t=n+1
x=n-1
if (n>=2 and n<=20):
    for i in range(0,x,1):
        print(" ",end ="")
        for j in range(0,x,1):
            print(" *",end ="")
        print('\n', end = '')
    for i in range(t,0,-1):
        for s in range(i,t,1):
            print(" ",end ="")

        for j in range (1,i+1,1):
            print("* ",end="")
        print('\n', end = '')
