#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[1] * n] * m
        
        for row in range(1, m):
            for col in range(1, n):
                
                ways[row][col] = ways[row - 1][col] + ways[row][col - 1]
        
        return ways[m-1][n - 1]

# @lc code=end

