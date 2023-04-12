class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        count = 0
        
        
        def dfs(node):
            nonlocal graph
            nonlocal visited
            
            visited.add(node)
            

            for child in graph[node]:
                
                if child not in visited:
                    dfs(child)
                    
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    graph[row + 1].append(col + 1)
                    
        for ele in graph:
            if ele not in visited:
                
                dfs(ele)
                count += 1

        
        return count
         
            
        
                    
