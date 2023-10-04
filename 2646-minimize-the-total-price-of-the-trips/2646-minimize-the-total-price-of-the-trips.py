class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = defaultdict(int)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
            
        for start,end in trips:
            predecessor = {}
            queue = deque([start])
            is_End = False
            predecessor[start] = -1
            parents = set()
            
            while queue:
                level = len(queue)
                
                for _ in range(level):
                    cur_node = queue.popleft()
                    
                    if cur_node == end:
                        is_End = True
                        break
                        
                    for child in graph[cur_node]:
                        if child not in parents:
                            predecessor[child] = cur_node
                            queue.append(child)
                            parents.add(cur_node)
                
                if is_End:
                    break
                            
            if is_End:
                node = end
                while node != -1:
                    count[node] += 1
                    node = predecessor[node]
                        
        
        memo = {}
        
        def dp(cur_node, halved, parent):
            if (cur_node, halved) in memo:
                return memo[(cur_node, halved)]
            
            ans = 0
            for next in graph[cur_node]:
                if next != parent:

                    if halved:
                        ans += ((price[next] * count[next] )+ dp(next, not halved, cur_node))  
                    else:
                        ans +=min(((price[next] // 2) * count[next]) + dp(next, not halved, cur_node), (price[next] * count[next])+ dp(next, halved, cur_node))
                         
                        
                    
                    
                    
            memo[(cur_node, halved)] = ans
            return ans  
            
        
        include = dp(0, True, -1) + ((price[0] // 2) * count[0])
        notInclude = dp(0, False, -1) + ((price[0]) * count[0])
        
        return min(include, notInclude)