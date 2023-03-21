class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        right = len(nums)
        left = 0
        
        
        while left < right:
            mid = left + (right - left)//2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
                
                
        return left