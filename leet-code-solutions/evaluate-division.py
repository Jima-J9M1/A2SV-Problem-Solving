class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for (start, end), val in zip(equations, values):
            graph[start].append((end, val))
            graph[end].append((start, 1/val))
            
        
        def djkstra(graph, start):
            distance = {i:float("inf") for i in graph}
            queue = [(start, 1)]
            distance[start] = 1
            visited = set()
            
            while queue:
                current_node, current_dis = heappop(queue)
                
                if current_node in visited:
                    continue
                    
                    
                for next_node, val in graph[current_node]:
                    w = val * current_dis
                    
                    if w < distance[next_node]:
                        distance[next_node] = w
                        heappush(queue, (next_node, w))
                        
            
            return distance
        
        ans = []
        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1)
                continue
                
            res = djkstra(graph, start)
            
            if res[end] == float("inf"):
                ans.append(-1)
                continue
                
            ans.append(res[end])
            
            
            
        return ans
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            