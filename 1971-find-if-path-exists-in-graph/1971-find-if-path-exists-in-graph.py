class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for edge in edges:
            vertex_1, vertex_2 = edge
            graph[vertex_1].append(vertex_2)
            graph[vertex_2].append(vertex_1)
            
        ans = self.dfs(graph, visited, source, destination )
        
        return ans
        
    def dfs(self, graph, visited, vertex, destination):
        if vertex == destination:
            return True
        
        visited.add(vertex)
        
        for neighbour in graph[vertex]:
            
            if neighbour not in visited:
                found = self.dfs(graph, visited, neighbour, destination)
                
                if found:
                    return True
                
                
        return False
        
        
        