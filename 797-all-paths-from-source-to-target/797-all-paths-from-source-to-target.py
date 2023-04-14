class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = [[]]
        path = [0]
        self.dfs(graph, 0, path, result)
        
        return result[0]
        
    def dfs(self,graph, idx, path, result):
        if path and path[-1] == len(graph) - 1:
            result[0].append(path[:])
            return 
            
        
        
        for ele in graph[idx]:
            self.dfs(graph, ele, path + [ele], result)
            
        return