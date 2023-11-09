class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # [[]], 0        
        brick_wall = {}
        max_width = sum(wall[0])
        
        for row in wall:
            width = 0
            
            for col in row:
                width += col
                if width == max_width:
                    continue
                    
                if width in brick_wall:
                    brick_wall[width] += 1
                else:
                    brick_wall[width] = 1
        
        if not brick_wall:
            return len(wall)
        
        
        max_freq = max(brick_wall.values())

        return len(wall) - max_freq
            
    
    