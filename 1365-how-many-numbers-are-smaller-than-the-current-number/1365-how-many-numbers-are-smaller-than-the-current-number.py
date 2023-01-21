class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        res = []
        for index in range(len(nums)):
            
            count = 0
            for j in range(len(nums)):
                if nums[index] > nums[j]:
                    count += 1
                
            res.append(count)
            
        
        return res