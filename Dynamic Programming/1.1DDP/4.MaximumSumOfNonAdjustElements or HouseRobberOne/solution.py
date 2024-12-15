#problem Link: https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #return self.Recursion(nums,len(nums)-1)
        #dp=[-1]*len(nums)
        #return self.Memmorization(nums,len(nums)-1,dp)
        return self.TabulationWithSpaceOptimisation(nums)

    def Recursion(self,nums,n): #1,2,3,4
        if n==0:
            return nums[0]
        
        skip=self.Recursion(nums,n-1) # 1
        if n==1:
            jump=nums[1]
        else:
            jump=nums[n]+self.Recursion(nums,n-2) #6
        return max(skip,jump) # 2
    
    def Memmorization(self,nums,n,dp):
        if n==0:
            return nums[0]
        
        if dp[n]!=-1:return dp[n]
        skip=self.Memmorization(nums,n-1,dp)
        if n==1:
            jump=nums[1]
        else:
            jump=nums[n]+self.Memmorization(nums,n-2,dp) #6
        dp[n]=max(skip,jump)
        return dp[n] 
    
    def Tabulation(self,nums,n,dp):
        dp[0]=nums[0]

        for i in range(1,nums+1):
            skip=dp[i-1] #4
            if i==1: 
                jump=nums[1] 
            else:
                jump=nums[i]+dp[i-2] #4+2=6
            dp[i]=max(skip,jump) #4
        return dp[n]
    
    def TabulationWithSpaceOptimisation(self,nums):
        first,second=nums[0],nums[0]

        for i in range(1,len(nums)):
            skip=second #4
            if i==1: 
                jump=nums[1] 
            else:
                jump=nums[i]+first 
            third=max(skip,jump)
            first=second
            second=third
        return second