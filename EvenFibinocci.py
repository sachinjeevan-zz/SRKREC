n=int(input())
a,b=2,8
print(a,b,end=" ")
c=4*b+a
while(c<=n):
    print(c,end=" ")
    a,b=b,c
    c=4*b+a