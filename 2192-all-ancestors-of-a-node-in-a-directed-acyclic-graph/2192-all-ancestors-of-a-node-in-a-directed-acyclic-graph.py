class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestor = [set() for _ in range(n)]
        incoming = [0]*n
        queue = deque()
        
        
        for edge in edges:
            v1, v2 = edge
            graph[v1].append(v2)
            incoming[v2] += 1
            
            
        for income in range(len(incoming)):
            
            if incoming[income] == 0:
                queue.append(income)
                
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                
                incoming[neighbor] -= 1
                ancestor[neighbor].add(node)
                
                
                ancestor[neighbor] = ancestor[neighbor].union(ancestor[node])
                                
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                 
        
        result  = [sorted(list(ele)) for ele in ancestor]
        
        return result

        