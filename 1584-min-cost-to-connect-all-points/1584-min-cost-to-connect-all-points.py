class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        def find(point):
            root = point
            
            while root != rep[root]:
                root = rep[root]
                
            while point != root:
                parent = rep[point]
                rep[point] = root
                point = parent
                
                
            return root
        
        def union(rep, size, point1, point2):
            parent_p1 = find(point1)
            parent_p2 = find(point2)
            
            if parent_p1 == parent_p2:
                return False
            
            if size[parent_p1] > size[parent_p2]:
                rep[parent_p2] = parent_p1
                
            elif size[parent_p2] > size[parent_p1]:
                rep[parent_p1] = parent_p2
            else:
                rep[parent_p2] = parent_p1
                size[parent_p1] += 1
                
            return True
        
        
        def diff(p1, p2, p3, p4):
            return abs(p1 - p2) + abs(p3 - p4)
        
        
        
        graph = []
        
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                manhattan = diff(points[i][0], points[j][0], points[i][1], points[j][1])
                graph.append([i, j, manhattan])
                
                
        graph.sort(key=lambda x: x[2])
        rep = {i: i for i in range(len(points))}
        size = [1] * len(points)
        
        count = 0
        result = 0
        
        for i in graph:
            p1, p2, cost = i
            
            if count == len(points) - 1:
                break
                
            if union(rep,size, p1, p2):
                result += cost
                count += 1
            else:
                continue
                
                
        return result
                
        
        
        
        
        
        
        
        
        
        
        