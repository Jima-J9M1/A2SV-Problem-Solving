class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        graph_rep = defaultdict(list)
        
        for row in range(len(graph)):
            for col in graph[row]:
                graph_rep[row].append(col)
                
        #bipartite 
        colors = [-1] * len(graph)
        
        for key in range(len(graph)):
            if colors[key] == -1:
                if not self.dfs(key, graph_rep, colors, 0):
                    return False
                
        return True
        
        
    def dfs(self,node, graph, colors, color):
        colors[node] = color
        
        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                if not self.dfs(neighbor, graph, colors, 1 - color):
                    return False
                
            elif colors[neighbor] == color:
                return False
        
        return True
                