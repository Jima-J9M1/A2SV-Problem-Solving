class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ans = 0
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans = abs(num)
            
            else:
                nums[abs(num) - 1] *= -1
                
        return ans