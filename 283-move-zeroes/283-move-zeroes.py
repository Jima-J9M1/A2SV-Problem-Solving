class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        length = len(nums)
        
        while right < length:
            
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                
            else:
                right += 1
                
    