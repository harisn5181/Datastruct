#https://www.geeksforgeeks.org/problems/geek-jump/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geek-jump

import sys

class Solution:
    
    #Base Function
    def minimumEnergy(self, arr, n):
        dp = [-1] * n
        return self.funcWithRecursion(n - 1, arr, dp)
    
     # 1. Recursion without Memoization
    def funcWithRecursion(self, n, arr, dp):
        if n == 0:
            return 0
        
        # One Jump (going from arr[n-1] to arr[n])
        oneJump = abs(arr[n] - arr[n - 1]) + self.funcWithRecursion(n - 1, arr, dp)
        
        # Two Jumps (going from arr[n-2] to arr[n])
        twoJump = sys.maxsize
        if n != 1:
            twoJump = abs(arr[n] - arr[n - 2]) + self.funcWithRecursion(n - 2, arr, dp)
        
        return min(oneJump, twoJump)
    
    # Time Complexity: O(2^n) due to recursion and overlapping subproblems
    # Space Complexity: O(n) due to recursive call stack
    
    # 2. Memoized Recursion (Top-down DP)
    def funcWithMemmorization(self, n, arr, dp):
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        
        # One Jump (going from arr[n-1] to arr[n])
        oneJump = abs(arr[n] - arr[n - 1]) + self.funcWithMemmorization(n - 1, arr, dp)
        
        # Two Jumps (going from arr[n-2] to arr[n])
        twoJump = sys.maxsize
        if n != 1:
            twoJump = abs(arr[n] - arr[n - 2]) + self.funcWithMemmorization(n - 2, arr, dp)
        
        dp[n] = min(oneJump, twoJump)
        return dp[n]
    
    # Time Complexity: O(n) because each subproblem is solved only once
    # Space Complexity: O(n) for the dp array and recursion stack
    
    # 3. Tabulation (Bottom-up DP)
    def funwithTabulation(self, n, arr, dp):
        dp[0] = 0
        for i in range(1, n + 1):
            # One Jump (going from arr[i-1] to arr[i])
            oneJump = abs(arr[i] - arr[i - 1]) + dp[i - 1]
            
            # Two Jumps (going from arr[i-2] to arr[i])
            twoJump = sys.maxsize
            if i != 1:
                twoJump = abs(arr[i] - arr[i - 2]) + dp[i - 2]
            
            dp[i] = min(oneJump, twoJump)
        return dp[n]
    
    # Time Complexity: O(n) because we iterate once through the array and solve each subproblem once
    # Space Complexity: O(n) for the dp array
    
    # 4. Tabulation with Space Optimization (Only keeping track of two values)
    def funwithTabulationWithSpaceOptimisationOne(self, n, arr, dp):
        if n == 0:
            return 0
        elif n == 1:
            return abs(arr[1] - arr[0])
        elif n >= 2:
            first = 0
            second = abs(arr[1] - arr[0])
            for i in range(2, n + 1):
                third = min(abs(arr[i] - arr[i - 1]) + second, abs(arr[i] - arr[i - 2]) + first)
                first, second = second, third
            return second
    
    # Time Complexity: O(n) due to the single iteration over the array
    # Space Complexity: O(1) since we only use two variables (first and second) to store the results
    
    # 5. Tabulation with Space Optimization (Using two variables for prev and prev2)
    def funwithTabulationWithSpaceOptimisationTwo(self, n, arr, dp):
        n = n + 1
        prev = 0
        prev2 = 0
        for i in range(1, n):
            jumpTwo = sys.maxsize
            jumpOne = prev + abs(arr[i] - arr[i - 1])
            if i > 1:
                jumpTwo = prev2 + abs(arr[i] - arr[i - 2])
            
            cur_i = min(jumpOne, jumpTwo)
            prev2 = prev
            prev = cur_i
        return prev
    
    # Time Complexity: O(n) due to the single iteration over the array
    # Space Complexity: O(1) since we only use two variables (prev and prev2) to store the results

# Test case
frogJump = Solution()
print(frogJump.minimumEnergy([10,15,25,40], 4))