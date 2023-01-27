class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right = 1
        read = 1
        
        
            
        if len(nums) > 1:
            for read in range(len(nums)):
                if nums[right - 1] != nums[read]:
                    nums[right] = nums[read]
                    right += 1

            while right < len(nums):
                nums.pop()

#         left = 0
#         count = 0
        
#         while left < len(nums) - 1:
#             if nums[left] == nums[left + 1]:
#                 nums[left] = 200
#                 count += 1
#                 continue
                
#             left += 1
            
#         nums.sort()
#         nums = nums[:-count]
#         print(nums)

            