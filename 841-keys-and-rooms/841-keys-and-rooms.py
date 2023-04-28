class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        graph = defaultdict(list)
        visited = {0}
        path = 0

        for indx in range(len(rooms)):
            graph[indx].extend(rooms[indx])
            
        
        
        while queue:
            len_level = len(queue)
            
            for _ in range(len_level):
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        path += 1
                        
        if path == len(rooms) - 1:
            return True
        
        return False
                        
                    