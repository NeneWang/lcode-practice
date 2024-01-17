#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
import pprint

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        # TOO SLOW
        # def backtrack(i1: int, i2: int, s1:str, s2:str, target:str, ti: int):
        #     if (i1 == len(s1) and i2==len(s2) and i1 + i2 == len(target)):
        #         return True
            
        #     if(i1 + i2 > len(target)):
        #         return False
            
        #     # print(f'checking for {s1[i1]} and {s2[i2]} if matches {target[ti]}')
        #     ress1 = ress2 = False
        #     if i1 < len(s1) and s1[i1] == target[ti]:
        #         ress1 = backtrack(i1 + 1, i2, s1, s2, target, ti + 1)

        #     if i2 < len(s2) and s2[i2] == target[ti]:
        #         ress2 = backtrack(i1, i2 + 1, s1, s2, target, ti + 1)
            
        #     if (ress1 or ress2):
        #         return True
        #     return False
        
        # if (len(s1) + len(s2) > len(s3)):
        #     return False

        # return backtrack(0, 0, s1, s2, s3, 0)
        
        len1, len2, len3 = len(s1), len(s2), len(s3)
        
        if len1 + len2 != len3:
            return False
        
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True
        
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        pprint.pprint(dp)
        print('===========================')
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        
        pprint.pprint(dp)
        print('===========================')

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                print( 'row', i, j, f"{dp[i - 1][j]}", dp[i - 1][j], 
                    '| s1[i - 1] == s3[i + j - 1]', f'{s1[i - 1]} {s3[i + j - 1]}',  s1[i - 1] == s3[i + j - 1],
                    '| dp[i][j - 1]',  dp[i][j - 1],
                    '| s2[j - 1] == s3[i + j - 1]', f'{s2[j - 1]} {s3[i + j - 1]}', s2[j - 1] == s3[i + j - 1],
                      '|| ', dp[i][j])
        

        pprint.pprint(dp)
        return dp[-1][-1]




# @lc code=end

