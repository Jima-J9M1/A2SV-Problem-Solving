class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(target):
            if target == 0:
                return 1
            
            if target in memo:
                return memo[target]
            
            if target < 0:
                return 0
            
            count = 0
            for i in range(len(nums)):
                count += dp(target - nums[i])
                
            memo[target] = count
            
            return memo[target]
        
        
        dp(target)
        
        
        return memo[target]