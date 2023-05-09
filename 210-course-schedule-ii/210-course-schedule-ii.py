class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * numCourses
        queue = deque()
        order = []
        for v1, v2 in prerequisites:
            graph[v2].append(v1)
            degree[v1] += 1
        
        
        for indx,ele in enumerate(degree):
            if ele == 0:
                queue.extend([indx])
        
        while queue:
            
            course = queue.popleft()
            order.append(course)
            
            for neighbor in graph[course]:
                
                degree[neighbor] -= 1
                
                if degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(order) != numCourses:
            return []
        
        
        return order
        