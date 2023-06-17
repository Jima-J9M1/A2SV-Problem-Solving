class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        n = len(nums)
        
        for i in range(1, target + 1):
            for j in range(n):
                if nums[j] <= i:
                    dp[i] = dp[i] + dp[i - nums[j]]
                    
        print(dp)
        
        return dp[target]
        
        
#         memo = {}
        
#         def dp(target):
#             if target == 0:
#                 return 1
            
#             if target in memo:
#                 return memo[target]
            
#             if target < 0:
#                 return 0
            
#             count = 0
#             for i in range(len(nums)):
#                 count += dp(target - nums[i])
                
#             memo[target] = count
            
#             return memo[target]
        
        
#         dp(target)
        
        
#         return memo[target]