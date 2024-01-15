#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:

        if n < 2:
            return 1

        memo = [0]*(n+1)
        memo[0] = memo[1] = 1

        if n < 2:
            return memo[n]
        
        for ci in range(2, n + 1):            
            if (ci%2 == 1):
                memo[ci] += memo[ci//2]**2
            for i in range(ci // 2):
                memo[ci] += 2 * memo[ci - (i + 1)] * memo[i]
            
        
        return memo[n] 
                

# @lc code=end

