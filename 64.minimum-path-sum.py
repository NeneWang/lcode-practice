#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # Find the right and down by chooing top or left and then + 1
        ROWS = len(grid)
        COLS = len(grid[0])
    


        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue

                candtop = grid[r-1][c] 
                candleft = grid[r][c-1]

                if r == 0:
                    grid[r][c] += candleft
                elif c == 0:
                    grid[r][c] += candtop 
                else:
                    grid[r][c] += min(candtop, candleft)    

        return grid[ROWS - 1][COLS - 1]


# @lc code=end

