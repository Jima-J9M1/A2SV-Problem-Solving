class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonal = {}
        
        #check if the row - col value is equal          
        for row in range(len(matrix)):
            
            for col in range(len(matrix[0])):
                
                if (row - col) in diagonal:
                    if diagonal[row - col] != matrix[row][col]:
                        return False
                    continue
                    
                diagonal[row - col] = matrix[row][col]

        
        return True
        