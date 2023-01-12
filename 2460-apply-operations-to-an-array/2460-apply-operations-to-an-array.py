class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = 1
        length = len(nums)
        count = 0
        
        while right < length and left  < right:
            if nums[right] == nums[left]:
                nums[left] *= 2
                nums[right] = 0
            right += 1
            left += 1
        
        count_zero = nums.count(0)
        
        left = 0
        while count_zero > 0:
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                count_zero -= 1
                continue
            left += 1
            
        return nums
                
                
        
        