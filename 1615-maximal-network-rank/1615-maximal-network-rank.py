class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for v1, v2 in roads:
            graph[v1].append(v2)
            graph[v2].append(v1)            
        
        
        max_res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                result = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    result -= 1
                    
                max_res = max(max_res,result)
                
        return max_res