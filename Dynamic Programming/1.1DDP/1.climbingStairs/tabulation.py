#tc:0 (n)
#sc:0(n)
def fun(n,dp):
    for i in range(2,n+1):
        dp[i]= dp[i-1]+dp[i-2]
    return dp[n]
n=5
dp=[-1]*(n+1)
dp[0]=1
dp[1]=1
print(fun(n,dp))