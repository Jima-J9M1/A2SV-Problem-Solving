class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        degree = defaultdict(int)
        preCourse = {i: set() for i in range(numCourses)}
        courses = deque()
        
        
        for v1,v2 in prerequisites:
            graph[v1].add(v2)
            degree[v2] += 1
            
        for indx in range(numCourses):
            if degree[indx] == 0:
                courses.append(indx)
                
        while courses:
            length = len(courses)
            
            for _ in range(length):
                course = courses.popleft()
                for child in graph[course]:
                    preCourse[child].add(course)
                    preCourse[child].update(preCourse[course])
                    
                    degree[child] -= 1
                    
                    if degree[child] == 0:
                        courses.append(child)
                        
        answer = []
        for start, end in queries:
            if start in preCourse[end]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
        