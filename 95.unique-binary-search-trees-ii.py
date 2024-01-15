#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def copyTreeInc(node, val = 0):
            if not node or node.val is not None:
                return None
            print("Copying", node.val)
            copy = TreeNode(node.val + val)

            if(node.right is not None):
                copy.right = copyTreeInc(node.right, val)
            if(node.left is not None):
                copy.left = copyTreeInc(node.left, val)

            return copy
        
        def copyTreeIncEach(memoArr, val=0):
            res = []
            for memoTree in memoArr:
                res.append(
                    copyTreeInc(memoTree, val)
                )
            return res
        
        memo=[None for x in range(n + 1)]
        memo[0] = []
        memo[1] = [TreeNode(1)]
        memo[2] = [
                TreeNode(1, copyTreeIncEach(memo[1], 1)),
                TreeNode(1,None, copyTreeIncEach(memo[1], 1)),
        ]
        
        if(n <= 2):
            return memo[n]
        
        for size in range(3, n+1):
            res = []
            # Do the res appenditure.
            # Do now teice for each case
            for middleVal in range(1, size + 1):
                treeCombinations = []
                
                
                # Is odd and we are on the middle.
                # if treeC == size // 2 + 1 and size % 2 == 1:
                print(f"======== {middleVal}")
                print(f" Left Using {middleVal - 1}", memo[middleVal - 1])
                leftTs = copyTreeIncEach(memo[middleVal - 1])
                
                print(f" Right Using {(size- middleVal)}", memo[(size- middleVal)])
                rightTs = copyTreeIncEach(memo[(size- middleVal)], middleVal) # Shoud get each there,and add the expected value.

                leftTs.append(None)
                rightTs.append(None)
                for leftT in leftTs:
                    for rightT in rightTs:
                        treeCombinations.append(
                            TreeNode(middleVal, leftT, rightT)
                        )
                res.extend(treeCombinations)
            memo[size] = res
            print("Storing", size, 'into memory', memo[size])
        
        # print(memo[n])
        return memo[2]


# @lc code=end

