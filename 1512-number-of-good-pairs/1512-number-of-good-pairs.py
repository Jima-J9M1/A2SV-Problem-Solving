class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = 0
        length = len(nums)
        
        for index in range(length):
            left = index + 1
            
            while left < length:
                
                if nums[index] == nums[left]:
                    count += 1
                left += 1
                
        return count