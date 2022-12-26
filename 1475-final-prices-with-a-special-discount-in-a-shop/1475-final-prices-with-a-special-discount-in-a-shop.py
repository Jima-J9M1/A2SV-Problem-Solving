class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for index in range(len(prices)):
            if not stack:
                stack.append(index)
            else:
                while stack and prices[stack[-1]] >= prices[index]:
                    indx = stack.pop()
                    prices[indx] -= prices[index]
                stack.append(index)
                
        
        return prices
        