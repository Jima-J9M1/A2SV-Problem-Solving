class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        rev = sorted(nums, reverse=True)
        sort = sorted(nums)
        
        if nums == rev or nums == sort:
            return True
        
        return False