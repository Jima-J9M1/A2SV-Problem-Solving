class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DAG - 0 to n - 1, graph contain the children node
        # return: all different path from 0 to n - 1
        
        n = len(graph) - 1
        res = []
        def dfs(node, path):
            if node == n:
                res.append(path[:])
                return
            
            for child in graph[node]:
                dfs(child, path + [child])
                
            return 
        
        
        dfs(0, [0])
        
        return res