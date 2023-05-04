class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[-1]
        
        
        for i in range(len(stones)):
            stones[i] *= -1
            
        heapq.heapify(stones)
        heapq.heapify(stones)
        
        while len(stones) > 1:
            val1 = -heapq.heappop(stones)
            val2 = -heapq.heappop(stones)
            
            y = max(val1, val2)
            x = min(val1, val2)
            
            if x  != y:
                res = y - x
                heapq.heappush(stones,-res)
        
        return -stones[-1] if stones else 0