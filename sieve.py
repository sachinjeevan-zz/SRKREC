import math
n = int(input())
lis = list(range(2,n+1))
i=0
while(lis[i]<=math.sqrt(n)):
    if(lis[i]!=0):
        for j in range(lis[i]**2-2,n-1,lis[i]):
            lis[j]=0
    i+=1
lis = list(filter(lambda a: a!=0,lis))
print(lis)