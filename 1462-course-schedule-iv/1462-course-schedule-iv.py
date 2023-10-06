class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        distance = [[False] * numCourses for _ in range(numCourses)]
        
        for start, end in prerequisites:
            distance[start][end] = True
            
        for i in range(numCourses):
            distance[i][i] = 0
            
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if not distance[i][j]:
                        distance[i][j] = distance[i][k] and distance[k][j]
                        
                        
        ans = []
        for start, end in queries:
            ans.append(distance[start][end])
            
        return ans
#         graph = defaultdict(set)
#         degree = defaultdict(int)
#         preCourse = {i: set() for i in range(numCourses)}
#         courses = deque()
        
        
#         for v1,v2 in prerequisites:
#             graph[v1].add(v2)
#             degree[v2] += 1
            
#         for indx in range(numCourses):
#             if degree[indx] == 0:
#                 courses.append(indx)
                
#         while courses:
#             length = len(courses)
            
#             for _ in range(length):
#                 course = courses.popleft()
#                 for child in graph[course]:
#                     preCourse[child].add(course)
#                     preCourse[child].update(preCourse[course])
                    
#                     degree[child] -= 1
                    
#                     if degree[child] == 0:
#                         courses.append(child)
                        
#         answer = []
#         for start, end in queries:
#             if start in preCourse[end]:
#                 answer.append(True)
#             else:
#                 answer.append(False)
                
#         return answer
        