#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # 1101/1101 cases passed (32 ms)
        # Your runtime beats 67.99 % of python3 submissions
        # Your memory usage beats 100 % of python3 submissions (12.7 MB)
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
        
# @lc code=end

