class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_val = float ("inf")
        ans = -1
        
        for index, val in enumerate(points):
            x1 , y1 = val
            distance = abs(x - x1) + abs( y - y1)
            if ((x1 == x) or (y == y1)) and (min_val > distance):
                min_val = distance
                ans = index
                
        return ans
        