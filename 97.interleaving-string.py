#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def backtrack(i1: int, i2: int, s1:str, s2:str, target:str, ti: int):
            if (i1 == len(s1) and i2==len(s2) and i1 + i2 == len(target)):
                return True
            
            if(i1 + i2 > len(target)):
                return False
            
            # print(f'checking for {s1[i1]} and {s2[i2]} if matches {target[ti]}')
            ress1 = ress2 = False
            if i1 < len(s1) and s1[i1] == target[ti]:
                ress1 = backtrack(i1 + 1, i2, s1, s2, target, ti + 1)

            if i2 < len(s2) and s2[i2] == target[ti]:
                ress2 = backtrack(i1, i2 + 1, s1, s2, target, ti + 1)
            
            if (ress1 or ress2):
                return True
            return False
        
        if (len(s1) + len(s2) > len(s3)):
            return False

        return backtrack(0, 0, s1, s2, s3, 0)
        
        




# @lc code=end

