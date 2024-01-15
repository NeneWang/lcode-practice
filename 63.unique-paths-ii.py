#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        ways = [[0] * COLS for x in range(ROWS)]
        # Compute first rows.

        has_bold = False
        for c in range(COLS):
            if obstacleGrid[0][c] == 1:
                has_bold = True
            if not has_bold:
                ways[0][c] = 1
        
        has_bold = False
        for r in range(ROWS):
            if obstacleGrid[r][0] == 1:
                has_bold = True
            if not has_bold:
                ways[r][0] = 1
            


        for r in range(1, ROWS):
            for c in range(1, COLS):
                if obstacleGrid[r][c] == 1:
                    ways[r][c] = 0
                else:
                    ways[r][c] = ways[r-1][c] + ways[r][c - 1]
        return ways[ROWS - 1][COLS - 1]

        
# @lc code=end

