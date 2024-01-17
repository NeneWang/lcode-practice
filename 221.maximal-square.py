#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

import pprint
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        ROWS, COLS = len(matxrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        max_side = 0

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "1":
                    dp[row][col] = min(
                        dp[row - 1][col],
                        dp[row][col - 1],
                        dp[row - 1][col - 1]
                    ) + 1 if row and col else 1
                    max_side = max(max_side, dp[row][col])

        return max_side * max_side

    
    
    

# @lc code=end

