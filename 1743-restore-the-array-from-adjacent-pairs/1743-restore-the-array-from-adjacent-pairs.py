class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        restored_arr = []
        visited = set()
        
        
        for start,end in adjacentPairs:
            graph[start].append(end)
            graph[end].append(start)
            indegree[start] += 1
            indegree[end] += 1
            
        for key in graph:
            if indegree[key] == 1 or indegree[key] == 0:
                queue.append(key)
                break
                
                
        while queue:
            adjacent  = queue.popleft()
            visited.add(adjacent)
            restored_arr.append(adjacent)
            
            for adj in graph[adjacent]:
                if adj not in visited:
                    queue.append(adj)
            
            
        return restored_arr
            
            
            
            
        