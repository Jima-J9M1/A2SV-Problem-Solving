class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        val = -1
        length = len(nums)
        
        nums.sort()
        
        # compare values of nums with the index of the loop through n size
        for index in range(length):
            
            if nums[index] != index:
                return index
            
        return length
        