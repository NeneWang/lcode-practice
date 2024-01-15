#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        COLS = len(word1) + 1
        ROWS = len(word2) + 1

        memo = [[0] * COLS for x in range(ROWS)]

        for row in range(ROWS):
            memo[row][0] = row
        for col in range(COLS):
            memo[0][col] = col

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if(word1[col -1] == word2[row-1]):
                    memo[row][col] = memo[row - 1][col - 1]
                else:
                    memo[row][col] = min(memo[row - 1][col - 1], 
                                         memo[row][col - 1],
                                         memo[row - 1][col]) + 1


        return memo[ROWS - 1][COLS - 1]


# @lc code=end

