class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_num = sum(nums)
        target = sum_num // 2
        
        if sum_num % 2 != 0:
            return False
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1,-1):
                dp[j] = dp[j] | dp[j - nums[i]]
                
        # print(dp)  
        return dp[target]