#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = [ [0] *  (COLS + 1) for _  in range(ROWS + 1)]

        max_side = 0
        # As long as we track the end corner of the figure, we can get the expected size. 
        for row in range(ROWS):
            for col in range(COLS):
                
                if(matrix[row][col] != '1'):
                    continue

                memo[row + 1][col + 1] = min(
                    memo[row][col + 1],
                    memo[row + 1][col],
                    memo[row][col]
                ) + 1
                max_side = max(max_side, memo[row + 1][col + 1])
        
        return max_side * max_side
        
        
# @lc code=end

