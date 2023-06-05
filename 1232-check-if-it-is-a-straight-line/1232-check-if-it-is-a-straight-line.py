class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
        change_y = y2 - y1
        change_x = x2 - x1
        
        for x3, y3 in coordinates[2:]:
            if change_y * (x3 - x1) != (y3 - y1) * change_x:
                return False

        return True
