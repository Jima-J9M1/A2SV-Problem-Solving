class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        curMax = dp[0]
        
        for i in range(2, len(nums)):
            dp[i] = curMax + nums[i]
            curMax = max(curMax, dp[i - 1])
            
            
        return max(dp)
        
        
        
        
        
        
        
        
#         memo = {}
        
    
#         def dfs(indx):
#             if indx not in memo:
#                 if indx >= len(nums):
#                     return 0



#                 rob = dfs(indx + 2) + nums[indx]
#                 not_rob = dfs(indx + 1)


#                 memo[indx] = max(rob, not_rob)
            
#             return memo[indx]
        
            
#         ans = dfs(0)
#         return ans
    
            
            
        