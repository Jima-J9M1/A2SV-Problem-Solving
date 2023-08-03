class Solution:
    def topologicalSort(self, nodes, graph, in_degree, matrix):
        queue = deque([node for node in nodes if node not in in_degree])
        
        ans = []
        indx = 0
        while queue:
            cur_node = queue.popleft()
            ans.append(cur_node)
            matrix[cur_node].append(indx)
            
            for neighbor in graph[cur_node]:
                in_degree[neighbor] -= 1
                
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            
            indx +=  1
            
        return ans
                    
                
                    
        
        
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        numbers = [i for i in range(1,k + 1)]
        matrix = defaultdict(list)
        
        
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        row_indegree = defaultdict(int)
        col_indegree = defaultdict(int)
        
        
        grid = [[0]*k for _ in range(k)]
        
        
        for start, end in rowConditions:
            row_graph[start].append(end)
            row_indegree[end] += 1
            
        for start, end in colConditions:
            col_graph[start].append(end)
            col_indegree[end] += 1
            
            
        row_ans = self.topologicalSort(numbers, row_graph, row_indegree, matrix) 
        col_ans = self.topologicalSort(numbers, col_graph, col_indegree, matrix) 
        
        if len(row_ans) != k or len(col_ans) != k:
            return []
        
        
        
        for key in matrix:
            row, col = matrix[key]
            grid[row][col] = key
            
        return grid
        
        
        
        
        
        
        
        
        
        
        
        
        
        