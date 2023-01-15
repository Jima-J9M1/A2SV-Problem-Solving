class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        new_mat = []
        
        #find new matrix for r and c 
        new_col = []
        for row in range(len(mat)):
            
            for col in range(len(mat[0])):
                new_col.append(mat[row][col])
                if c == len(new_col):
                    new_mat.append(new_col)
                    new_col = []
        
        return new_mat
                    
                
                