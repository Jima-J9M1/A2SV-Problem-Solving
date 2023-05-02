class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [0, -1], [1,0],[0,1]]
        queue = deque()
        result = [[0] * len(mat[0]) for i in range(len(mat))]
        
        
        
        def isbound(row, col):
            return ((0 <= row < len(mat)) and (0 <= col < len(mat[0])))
        

        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append([row, col])
                    
                    
                    
        while queue:
            len_level = len(queue)
            
            for _ in range(len_level):
                row, col = queue.popleft()
                
                for new_row, new_col in directions:
                    new_row += row
                    new_col += col
                    
                    if isbound(new_row, new_col) and mat[new_row][new_col] == 1:
                        mat[new_row][new_col] = 0
                        result[new_row][new_col] = result[row][col] + 1
                        queue.append([new_row, new_col])
                        
                
            
        return result
            
        
        
        