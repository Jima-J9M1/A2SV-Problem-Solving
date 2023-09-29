class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        grid = [[float("-inf")]*(len(dungeon[0]) + 1) for _ in range(len(dungeon) + 1)]
        m = len(dungeon)
        n = len(dungeon[0])
        
        if dungeon[-1][-1]  <= 0: grid[m -1][n -1] = -1 + dungeon[-1][-1]
        else: grid[m - 1][n - 1] = dungeon[-1][-1]
            
            
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1 , -1):
                if i == m - 1 and j == n - 1:
                    continue  
                val = max(grid[i + 1][j], grid[i][j + 1])
                
                if val > 0:
                    if dungeon[i][j] <= 0:
                        grid[i][j] = dungeon[i][j] - 1
                    else:
                        grid[i][j] = dungeon[i][j]     
                else:
                    grid[i][j] = -1 if dungeon[i][j] + val == 0 else dungeon[i][j] + val
            
        return -grid[0][0] if grid[0][0] < 0 else 1
                