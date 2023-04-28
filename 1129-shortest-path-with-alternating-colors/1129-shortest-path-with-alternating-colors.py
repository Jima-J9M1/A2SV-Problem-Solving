class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        queue = deque([[0,3]])
        graph = defaultdict(list)
        answer = [-1] * n
        level = 0
        visited = {(0,3)}      
        
        for edge in redEdges:
            ai, bi = edge
            graph[ai].append([bi,0])
        
        for edge in blueEdges:
            v1, v2 = edge
            graph[v1].append([v2,1])
            
        while queue:
            len_level = len(queue)
            
            for __ in range(len_level):
                node, color = queue.popleft()
                if answer[node] == -1:
                    answer[node] = level
                
                for neighbor in graph[node]:
                    if color != neighbor[1] and tuple(neighbor) not in visited:
                        queue.append(neighbor)
                        visited.add((neighbor[0], neighbor[1]))
                        
            
            level += 1
            
            
        return answer
                        
                
            
                
                