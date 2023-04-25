class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for indx in range(len(bombs) - 1):
            for j in range(indx + 1, len(bombs)):
                distance = self.distance(bombs[indx], bombs[j])
                if distance <= bombs[indx][2]:
                    graph[indx].append(j)

                if distance <= bombs[j][2]:
                    graph[j].append(indx)
                    
        max_val = 0
        for indx in range(len(bombs)):
            visited =  [set()]
            self.dfs(graph, indx, visited)
            max_val = max(len(visited[0]), max_val)
            
        return max_val
        
    def distance(self,bomb1, bomb2):
        return ((bomb1[0] - bomb2[0])**2 + (bomb1[1] - bomb2[1])**2) ** 0.5
    
    def dfs(self, graph, node, visited):
        if node in visited[0]:
            return
        
        visited[0].add(node)
        
        for child in graph[node]:
            
            if child not in visited[0]:
                self.dfs(graph, child, visited)
        
        return 