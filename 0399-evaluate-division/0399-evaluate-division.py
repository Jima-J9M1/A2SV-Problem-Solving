class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dijkstra(graph, start):
            calculation = {node:float("inf") for node in graph}
            calculation[start] = 1
            visited = set()
            prority_queue = [(start, 1)]
            
            while prority_queue:
                current_node, current_val = heappop(prority_queue)
                
                if current_node in visited:
                    continue
                    
                visited.add(current_node)
                
                for neighbor, weight in graph[current_node]:
                    w = current_val * weight
                    
                    if w < calculation[neighbor]:
                        calculation[neighbor] = w
                        heappush(prority_queue, (neighbor, w))
                        
            return calculation
        
        
        graph = defaultdict(list)
        
        for equ, val in zip(equations, values):
            start, end = equ
            graph[start].append((end, val))
            graph[end].append((start, 1/val))
           
        ans = []
        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1)
                continue
                
            cal = dijkstra(graph, start)
            
            if cal[end] == float('inf'):
                ans.append(-1)
                continue
                
            
            ans.append(cal[end])
            
        return ans
            
            
            
            
            
            
            
            