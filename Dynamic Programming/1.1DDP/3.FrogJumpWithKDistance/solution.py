import sys

class Solution:
    def minimizeCost(self, k, arr): 
        n = len(arr)
        dp = [0] * n
        return self.funwithTabulation(k, arr, n - 1, dp)
    
    # Recursion (Brute Force)
    def funcWithRecursion(self, k, arr, dp, n):
        if n == 0:
            return 0
        minJumpValue = sys.maxsize
        for i in range(1, k + 1):
            if n - i < 0:
                continue
            minJumpValue = min(minJumpValue, abs(arr[n] - arr[n - i]) + self.funcWithRecursion(k, arr, dp, n - i))
        return minJumpValue
    
    # Time Complexity: O(k^n) due to recursive calls (exponential growth of subproblems).
    # Space Complexity: O(n) due to recursion stack depth.
    
    # Memoization (Top-Down DP)
    def funcWithMemmorization(self, k, arr, dp, n):
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        minJumpValue = sys.maxsize
        for i in range(1, k + 1):
            if n - i < 0:
                continue
            minJumpValue = min(minJumpValue, abs(arr[n] - arr[n - i]) + self.funcWithMemmorization(k, arr, dp, n - i))
        dp[n] = minJumpValue
        return minJumpValue
    
    # Time Complexity: O(n * k) because we solve each subproblem once and have at most `k` choices for each subproblem.
    # Space Complexity: O(n) for the dp array and recursion stack.
    
    # Tabulation (Bottom-Up DP)
    def funwithTabulation(self, k, arr, length, dp):
        # Base case for the first stone
        dp[0] = 0
        
        for n in range(1, length + 1):
            minJumpValue = sys.maxsize
            for i in range(1, k + 1):
                if n - i < 0:
                    continue
                minJumpValue = min(minJumpValue, abs(arr[n] - arr[n - i]) + dp[n - i])
            dp[n] = minJumpValue
        return dp[length]
    
    # Time Complexity: O(n * k) because for each stone, we are checking up to `k` previous stones.
    # Space Complexity: O(n) due to the dp array.


frogJumpWithK = Solution()
print(frogJumpWithK.minimizeCost(2,[10,15,25,40]))