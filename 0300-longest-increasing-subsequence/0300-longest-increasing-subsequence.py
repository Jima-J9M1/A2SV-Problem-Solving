class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            ans = 0
            
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    ans = max(ans, dp[j])
                    
            dp[i] += ans
            
        
                    
        return max(dp)
                    
                