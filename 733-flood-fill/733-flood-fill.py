class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[-1,0], [0,-1], [1, 0], [0, 1]]
        def isbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
        
        
        def dfs(row, col, color,turn):
            if image[row][col] == color or image[row][col] != turn:
                return 
            
            image[row][col] = color
            
            for new_row, new_col in directions:
                new_row += row
                new_col += col
                
                if isbound(new_row, new_col):
                    dfs(new_row, new_col,color, turn)
                    
            
        dfs(sr,sc,color, image[sr][sc])
        
        return image
                    
        
                    
                
                
                