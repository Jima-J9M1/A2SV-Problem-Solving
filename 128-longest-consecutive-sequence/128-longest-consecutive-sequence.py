class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        diff = 0
        count = 0
        max_val = 0
        
        if len(nums) == 0:
            return 0
        

        for index in range(len(nums)-1):
            if nums[index + 1] == nums[index]:
                continue
                
            diff = nums[index + 1] - nums[index]
            if diff == 1:
                count += 1
            else:
                max_val = max(max_val, count)
                count = 0
        max_val = max(max_val,count)
                
        return max_val + 1
        
        
