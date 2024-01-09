#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if(x < 2):
            return x
        
        left = 2
        right = x

        while(left <= right):
            # get the mid point and go moving around
            mid = (right - left) // 2 + left
            num = mid * mid

            if(num > x):
                right = mid - 1
            elif(num < x):
                left = mid + 1
            else:
                return mid

        return right

        
# @lc code=end

