class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for ele in matrix:
            row_set = set(ele)
            
            if target in ele:
                return True
        