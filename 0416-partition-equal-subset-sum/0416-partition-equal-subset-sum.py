class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        
        @cache
        def dp(indx, _sum):
            if _sum == target:
                return True
            
            
            if indx >= len(nums):
                return False
            
            
            if _sum > target:
                return False
            
            
            return dp(indx + 1, _sum + nums[indx]) or dp(indx + 1, _sum)
            
        
        
        return dp(0, 0)
            
            
            