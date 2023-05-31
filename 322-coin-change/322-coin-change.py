class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
        
#         if len(coins) == 1:
#             return amount if amount == coins[-1] else -1
        
        arr = [-1] * (amount + 1)
        arr[0] = 0

        
        for i in range(1, amount + 1):
            for ele in coins:
                coin = i - ele
                if coin >= 0 and arr[coin] != -1:
                    if arr[i] != -1:
                        arr[i] = min(arr[coin] + 1, arr[i])
                        
                    else:
                        arr[i] = arr[coin] + 1
                        
        return arr[amount]
                    
                    
                    