class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = prices[0]
        min_val = prices[0]
        profit = 0
        for price in prices:
            if max_val > price or min_val > price:
                profit += (max_val - min_val)
                max_val = price
                min_val = price
            else:
                max_val = price
        profit += (max_val - min_val)
        return profit
                
        
        