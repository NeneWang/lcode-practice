#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # Traverse each.
        COLS = len(s)
        ROWS = COLS + 1

        memo = [0] * ROWS
        memo[0] = memo[1] = 1

        for row in range(2, ROWS):

            if s[row-1] != "0":
                memo[row] += memo[row - 1]
            if("10" <= s[row - 2: row] <= "26"):
                memo[row] += memo[ row - 2]
        return memo[-1]



        
# @lc code=end

