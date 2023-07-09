class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        buildHeight = []
        n = len(heights)
        
        for i in range(n - 1):
            heightDiff = heights[i + 1] - heights[i]
            if heightDiff <= 0:
                continue
            heappush(buildHeight, heightDiff)
            
            if len(buildHeight) > ladders:
                bricks -= heappop(buildHeight)
            
            if bricks < 0:
                return i
            
        return n - 1
            
            