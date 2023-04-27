class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [[-1,0], [0, -1], [1, 0], [0, 1]]
        queue = deque()
        fresh = 0
        
        def isbound(grid, row, col):
            return (0 <= row < len(grid) and (0 <= col < len(grid[0])))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append([row, col])
                
                if grid[row][col] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        
        minute = 0
        
        while queue:
            minute += 1
            len_level = len(queue)
            
            for _ in range(len_level):
                row, col = queue.popleft()
                
                for new_row, new_col in directions:
                    new_row += row
                    new_col += col
                    
                    if isbound(grid, new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append([new_row, new_col])
                        fresh -= 1
                        
        if fresh == 0:  
            return minute - 1
        
        return -1
                