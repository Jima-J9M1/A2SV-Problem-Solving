class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        max_point = points[0][1]
        min_point = points[0][0]
        count = 1
        
        for indx in range(1, len(points)):
            
            if max_point >= points[indx][0]:
                min_point = points[indx][0]
            else:
                
                max_point = points[indx][1]
                min_point = points[indx][0]
                count += 1
                
        
        return count
                
            
        
        
        
        
        