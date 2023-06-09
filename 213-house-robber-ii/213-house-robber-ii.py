class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        robbery_one = self.dp(nums[:-1])
        robbery_two = self.dp(nums[1:])
        
        return max(robbery_one,robbery_two)
        
        
    def dp(self,nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        curMax = dp[0]
        
        for i in range(2, len(nums)):
            dp[i] = curMax + nums[i]
            curMax = max(curMax, dp[i - 1])
            
        return max(dp)
        
#         if len(nums) == 1:
#             return nums[-1]
        
#         return max(self.helper(nums[1:]),self.helper(nums[:-1]))
        
#     def helper(self, nums):
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