class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        for i in range(len(piles)):
            piles[i] *= -1
            
        heapify(piles)
        
        for _ in range(k):
            val = -heappop(piles)
            val -= math.floor(val / 2)
            heappush(piles, -val)
            
        return -sum(piles)