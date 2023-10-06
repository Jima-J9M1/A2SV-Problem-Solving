class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for start, end, w in times:
            graph[start].append([end, w])
            
        def dijkistra(graph, start):
            visited = set()
            distances = {node:float("inf") for node in range(1, n + 1)}
            distances[start] = 0
            
            prority_queue = [(0, start)]
            
            while prority_queue:
                current_dis, current_node = heappop(prority_queue)
                
                if current_node in visited:
                    continue
                    
                visited.add(current_node)
                
                for neighbor, weight in graph[current_node]:
                    distance = current_dis + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heappush(prority_queue, (distance, neighbor))
                        
            return distances
        
        dis = dijkistra(graph, k)
        
        
        
        return max(dis.values()) if max(dis.values()) != float("inf") else -1 
        
        