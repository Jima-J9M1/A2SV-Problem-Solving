class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache        
        def dp(indx, sum_):
            if indx == len(nums) and sum_ == target:
                return 1
            
            if indx >= len(nums):
                return 0
            
            
            minus = dp(indx + 1, sum_ + nums[indx])
            plus = dp(indx + 1, sum_ - nums[indx])
            
            return minus + plus
        
        ans = dp(0, 0)
  
        return ans
            
            