class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = 0
        
        indx = 0
        
        while indx < len(nums):
            postionOfValue = nums[indx] - 1
            
            if postionOfValue >= 0 and postionOfValue < len(nums) and postionOfValue != indx:
                nums[indx], nums[postionOfValue] = nums[postionOfValue], nums[indx]
                continue
                
            elif postionOfValue < 0 or postionOfValue >= len(nums):
                ans = indx + 1
            
            indx += 1
            
            
        return ans
            
        
