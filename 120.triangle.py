#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                minTop = 2**53
                if col > 0:
                    minTop = triangle[row - 1][col - 1]
                if col < row:
                    minTop = min(minTop, triangle[row - 1][col])
                triangle[row][col] += minTop
        return min(triangle[len(triangle) - 1])

        
# @lc code=endm

