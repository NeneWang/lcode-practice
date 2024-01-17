#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rightStream = [[0] * COLS for _ in range(ROWS)] 
        

        for row in range(ROWS):
            prev = 0
            for col in range(COLS):
                prev += matrix[row][col]
                rightStream[row][col] = prev

        self.rightStream = rightStream
        self.matrix = matrix

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            substract = self.rightStream[row][col1 - 1] if(col1 > 0) else 0
            sum += (self.rightStream[row][col2] - substract )
        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

