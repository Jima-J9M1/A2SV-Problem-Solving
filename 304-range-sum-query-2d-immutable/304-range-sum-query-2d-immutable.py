class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cols = len(matrix[0])
        rows = len(matrix)
        
        self.prfix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            
            for col in range(cols):
                
                self.prfix_sum[row + 1][col + 1] = self.prfix_sum[row + 1][col] + self.prfix_sum[row][col + 1] - self.prfix_sum[row][col] + matrix[row][col]
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = self.prfix_sum[row2 + 1][col2 + 1] - self.prfix_sum[row1][col2 + 1] - self.prfix_sum[row2 + 1][col1] + self.prfix_sum[row1][col1]
        
        return val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)