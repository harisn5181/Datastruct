#tc:0 (n)
#sc:0(n)+   0(n)recstackspace
def fun(n,dp):
    if n==0:return 1
    elif n==-1: return 0
    if(dp[n]!=-1):return dp[n]
    dp[n]= fun(n-1,dp)+fun(n-2,dp)
    return dp[n]
n=5
dp=[-1]*(n+1)
print(fun(n,dp))