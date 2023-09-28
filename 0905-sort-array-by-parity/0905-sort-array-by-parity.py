class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        right = len(nums) - 1
        left = 0
        
        while left < right:
            
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                
            else:
                left += 1
                
                
        return nums