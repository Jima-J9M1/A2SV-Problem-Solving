class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [[-1,0],[0,1],[0,-1],[1,0]]
        def isbound(row, col):
            return (0 <= row < len(maze)) and (0 <= col < len(maze[0]))
        
        queue = deque([entrance])
        min_val = float("inf")
        level = 0
        maze[entrance[0]][entrance[1]] = False
        flag = True
        
        while queue:
            len_level = len(queue)
            for i in range(len_level):
                row, col = queue.popleft()
                for new_row, new_col in directions:
                    new_row += row
                    new_col += col
                    
                    if not isbound(new_row, new_col):
                        if level != 0:
                            min_val = level
                            flag = False
                            break
                    elif isbound(new_row, new_col) and maze[new_row][new_col] == ".":
                        
                        queue.append([new_row, new_col])
                        maze[new_row][new_col] = False
                       
                    
                if not flag:
                    break
                    
            level += 1
                
                
                
            if not flag:
                break
                
        return min_val if min_val != float('inf') else -1
                
        
                        
            