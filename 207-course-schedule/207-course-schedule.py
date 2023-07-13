class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        degree = [0]*numCourses
        numSelectedCourses = []
        queue = deque()
        
        
        for v1, v2 in prerequisites:
            graph[v2].append(v1)
            degree[v1] += 1
        
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
                
        
                        
        while queue:
            node = queue.popleft()
            
            numSelectedCourses.append(node)
            
            for child in graph[node]:
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)
                    
        if len(numSelectedCourses) == numCourses:
            return True
        
        # print(numSelectedCourses)
        return False