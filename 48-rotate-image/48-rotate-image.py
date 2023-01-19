class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left,right  = 0, len(matrix[0])
        top, bottom = 0, len(matrix) - 1
        
        while top <=  bottom:
            j = top
            
            while j < bottom:
                prev_row = j
                prev_col = left 
                prev_val = matrix[prev_row][prev_col]
                for _ in range(4):
                    
                    new_row = prev_col
                    new_col = len(matrix) - 1 - prev_row
  

                    temp = matrix[new_row][new_col]
                    matrix[new_row][new_col] = prev_val

                    
                    
                    prev_val = temp
                    prev_row = new_row
                    prev_col = new_col
                
                j += 1

                    
               
            top += 1
            left += 1
            bottom -= 1
            
                
                
                    
                    
                    
                