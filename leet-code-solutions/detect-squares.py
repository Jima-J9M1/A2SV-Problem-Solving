class DetectSquares:

    def __init__(self):
        self.cord = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.cord[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1,y1 = point
        
        ans = 0
        
        for x2,y2 in self.cord:
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            
            
            if dx == dy and dy > 0:
                point1 = (x1, y2)
                point2 = (x2, y1)
                
                if point1 in self.cord and point2 in self.cord:
                    ans += self.cord[(x2,y2)] * self.cord[point1] * self.cord[point2]
        
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)