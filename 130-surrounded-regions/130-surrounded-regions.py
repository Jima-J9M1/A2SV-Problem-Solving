class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1,0],[0,-1],[0,1],[1,0]]
        
        def isbound(row,col):
            return (0 <= row < len(board) and (0 <= col < len(board[0])))
        
        def dfs(row, col,result, visited):
            visited[row][col] = False
            result.append((row,col))
            for nrow, ncol in directions:
                nrow += row
                ncol += col
                
                if isbound(nrow, ncol):
                    if visited[nrow][ncol] and board[nrow][ncol] == 'O':
                        if not dfs(nrow, ncol, result, visited):
                            return False
                else:
                    return False
                
            return True
                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    visited = [[1 for _ in range(len(board[0]))] for _ in range(len(board))]
                    result = []
                    ans = dfs(row, col, result,visited)
                    
                    if ans:
                        for nrow,ncol in result:
                            board[nrow][ncol] = "X"
                        
        
