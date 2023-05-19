class Solution:
    def find(self, path):
        if path == self.rep[path]:
            return path
        
        ans = self.find(self.rep[path])
        self.rep[path] = ans
        
        return ans
        
    def union(self, path1, path2):
        path1_rep = self.find(path1)
        path2_rep = self.find(path2)
        
        if path1_rep != path2_rep:
            if self.size[path1_rep] > self.size[path2_rep]:
                self.rep[path2_rep] = path1_rep
            elif self.size[path1_rep] < self.size[path2_rep]:
                self.rep[path1_rep] = path2_rep
        
            else:
                
                self.rep[path2_rep] = path1_rep
                self.size[path1_rep] += 1
                
            
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = set()
        self.rep = {}

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.rep[(row,col)] = (row,col)
                
            
        
        self.size = defaultdict(int)
        
        neighbors = {
                  1: [(0, -1, {1, 4, 6}), (0, 1, {1, 3, 5})],
                  2: [(1, 0, {2, 5, 6}), (-1, 0, {2, 3, 4})],
                  3: [(0, -1, {1, 4, 6}), (1, 0, {2, 5, 6})],
                  4: [(1, 0, {2, 5, 6}), (0, 1, {1, 3, 4})],
                  5: [(-1, 0, {2, 3, 4}), (0, -1, {1, 4, 6})],
                  6: [(-1, 0, {2, 3, 4}), (0, 1, {1, 3, 5})]
              }
        
        
        
        def isbound(grid,row,col):
            return ((0 <= row < len(grid)) and (0 <=  col < len(grid[0])))
            
            
        for row, row_ele in enumerate(grid):
            for col, col_ele in enumerate(row_ele):
                    for connect in neighbors[col_ele]:
                        r,c = connect[0], connect[1]
                        r += row
                        c += col
                        if isbound(grid,r,c) and  grid[r][c] in connect[2] and (r,c) not in visited:
                            self.union((row, col), (r, c))
                            
            visited.add((row,col))
            
        ans = set()
        
        
            
        return self.find((0,0)) == self.find((len(grid) - 1, len(grid[0]) - 1))
                        
            
            