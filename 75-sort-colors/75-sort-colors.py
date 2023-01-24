class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(1,len(nums)):
            right = index
            val = nums[right]
            
            while right > 0 and nums[right - 1] > val:
                nums[right] = nums[right - 1]
                right -= 1
                
            nums[right] = val
        
        return nums