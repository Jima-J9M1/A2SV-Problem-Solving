class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        colors = [-1] * (n + 1)

        for row in range(len(dislikes)):
            ui, vi = dislikes[row]
            graph[ui].append(vi)
            graph[vi].append(ui)
 
        for key in range(1, n + 1):
            if colors[key] == - 1:
                if not self.dfs(key, graph, colors, 0):
                    return False
        
        return True
    
    
        
    def dfs(self, node, graph, colors, color):
        colors[node] = color
        
        for child in graph[node]:
            if colors[child] == -1:
                if not self.dfs(child, graph, colors, 1 - color):
                    return False
                
            elif colors[child] == color:
                return False
        
        return True
        