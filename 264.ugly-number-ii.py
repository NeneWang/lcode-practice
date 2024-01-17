#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = {1}

        for t in range(n):
            smallestuggly= heapq.heappop(heap)
            for i in [2, 3, 5]:
                computed = smallestuggly * i
                if computed not in visited:
                    visited.add(computed)
                    heapq.heappush(heap, computed)
        return smallestuggly

            


        
# @lc code=end

