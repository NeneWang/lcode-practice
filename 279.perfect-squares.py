#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
import math
class Solution:
    
    def numSquares(self, n: int) -> int:
        memo = [float('inf')] * (n + 1)
        memo[0] = 0
        squares = []
        # calculate up to upper bound
        for num in range(1, math.floor(math.sqrt(n) + 1)):
            squares.append(num * num)

        # print(squares)
        for target in range(1, n+1):
            for sqrt in squares:
                if(sqrt > target):
                    break
                memo[target] = min(
                    memo[target],
                    memo[target - sqrt] + 1
                )
            # print(target, memo[target])

        return memo[n]
        
# @lc code=end

