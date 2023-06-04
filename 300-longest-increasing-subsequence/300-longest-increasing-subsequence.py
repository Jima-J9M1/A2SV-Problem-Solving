class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(indx):
            if indx == 0:
                return 1

            if indx in memo:
                return memo[indx]
            
            max_length = 1
            for i in range(indx):
                if nums[indx] > nums[i]:
                    max_length = max(max_length, 1 + dp(i))
                
            memo[indx] = max_length
                
            return memo[indx]
        
        max_length = 1
        
        for indx in range(len(nums)):
            max_length = max(max_length, dp(indx))
            
        return max_length
