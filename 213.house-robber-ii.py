#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if(len(nums) == 1):
            return nums[0]
        
        left = self.rob_range(nums[1:])
        right = self.rob_range(nums[:-1])
        return max(left, right)

    def rob_range(self, nums: List[int]):
        [left, prevMax] = [0, 0]

        for num in nums:
            temp = prevMax # Since it will be used now.

            currentMax = left + num
            prevMax = max(currentMax, prevMax)
            left = temp
        return prevMax
    


            
        
# @lc code=end

