class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        degree = [0] * numCourses
        queue =deque()
        res = []
        for course, precourse in prerequisites:
            graph[precourse].append(course)
            degree[course] += 1
            
            
        for indx in range(len(degree)):
            if degree[indx] == 0:
                queue.append(indx)
                
        while queue:
            preCourse = queue.popleft()
            
            res.append(preCourse)
            
            for neighbor in graph[preCourse]:
                degree[neighbor] -= 1
                
                if degree[neighbor] == 0:
                    queue.append(neighbor)
                    
            
            
        if len(res) == numCourses:
            return True
        
        return False