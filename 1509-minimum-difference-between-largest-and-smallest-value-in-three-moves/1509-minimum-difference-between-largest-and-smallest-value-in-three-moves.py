class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) <= 4:
            return 0
        
        count = 0
        left = 3
        right = len(nums) - 1
        result = float("inf")
        
        while count <= 3:
            result = min(result, nums[right] - nums[left])
            left -= 1
            right -= 1
            count += 1
            
        return result
            
            
        