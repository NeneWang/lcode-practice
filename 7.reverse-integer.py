#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 10:
            return x
        
        if x%10 == 0:
            x//=10
        isnegative = False
        if x<0:
            x = -x
            isnegative = True
        
        #now thats cleaned, try string reverse it
        str_digits = str(x)[::-1]
        if(int(str_digits)>2**31):
            return 0
        return int(str_digits) if not isnegative else -int(str_digits)

        
# @lc code=end

