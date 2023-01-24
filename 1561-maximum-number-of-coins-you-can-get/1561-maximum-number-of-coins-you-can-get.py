class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        
        ptr1 = 1
        ptr2 = len(piles) - 1
        res = 0
        while ptr1 < ptr2:
            res += piles[ptr1]
            ptr1 += 2
            ptr2 -= 1
            
        return res
            
            