class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if len(matrix) == 1:
            if target in matrix[-1]:
                return True
            
        ans = False
        
        for col in range(1):
            
            for row in range(len(matrix)-1):
                
                if matrix[row][col] <= target and matrix[row+1][col] > target:
                    if target in matrix[row]:
                        ans = True
                    break
        
        if target in matrix[-1]:
            return True
        
        
                
        return ans
            
                
        
        
        
        
#         for ele in matrix:
#             row_set = set(ele)
            
#             if target in ele:
#                 return True
        