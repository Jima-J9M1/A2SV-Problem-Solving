class Solution:
    
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        ans = self.dp(nums,0,memo)
        return ans
        
    def dp(self,nums, indx, memo):
        if indx >= len(nums):
            return 0
        
        if indx == len(nums) - 1:
            return nums[indx]
        
        for i in range(indx, len(nums)):
            if (i + 2) not in memo:
                res = self.dp(nums, (i + 2), memo)
                memo[i] = res + nums[i]
                
            else:
                memo[i] = memo[i + 2] + nums[i]
                
                
            if (i + 1) not in memo:
                res = self.dp(nums,(i + 1), memo)
                memo[i + 1] = res
            
            return max(memo[i], memo[i + 1])
            
            
        