import math
n=int(input())
flag = True
if(n<=1):
    flag=False
elif(n>3 and (n%2==0 or n%3==0)):
    flag=False
k=1
a,b=6*k-1,6*k+1
while(flag and (a<=math.sqrt(n))):
    if(n%a==0 or n%b==0):
        flag=False
    k+=1
    a,b=6*k-1,6*k+1
if(flag):
    print("Prime")
else:
    print("Not a Prime")