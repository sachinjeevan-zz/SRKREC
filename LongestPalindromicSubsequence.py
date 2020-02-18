def printLPS(dp,i,j,s,ans,n):
    if(i<n and j>=0 and dp[i][j]>0):
        if(s[i]==s[j]):
            printLPS(dp,i+1,j-1,s,ans+s[i],n)
            dp[i][j]=dp[i][j]*-1
        else:
            if(dp[i][j-1]<0):
                if(dp[i][j-1]*-1<=dp[i+1][j]):
                    printLPS(dp,i+1,j,s,ans,n)
            if(dp[i][j-1]>dp[i+1][j]):
                printLPS(dp,i,j-1,s,ans,n)
                dp[i][j]=dp[i][j]*-1
            elif(dp[i+1][j]>dp[i][j-1]):
                printLPS(dp,i+1,j,s,ans,n)
                dp[i][j]=dp[i][j]*-1
            else:
                printLPS(dp,i,j-1,s,ans,n)
                printLPS(dp,i+1,j,s,ans,n)
                dp[i][j]=dp[i][j]*-1
    elif(dp[i][j]==0):
        if(dp[0][n-1]%2==0):
            print(ans+ans[::-1])
        else:
            print(ans+ans[-2::-1])

s = input()
n = len(s)
# [[1,2,3],[5,6,7],[8,9,10]]
dp=[]
l=[0]*n
for i in range(n):
    dp.append(l[::])
    dp[i][i]=1
k=1
while(k!=n):
    i,j=0,k
    while(j<n):
        if(s[i]==s[j]):
            dp[i][j]=dp[i+1][j-1]+2
        else:
            dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        i+=1
        j+=1
    k+=1
for j in dp:
    print(j)
i,j=0,n-1
ans=""
printLPS(dp,i,j,s,ans,n)
for j in dp:
    print(j)
