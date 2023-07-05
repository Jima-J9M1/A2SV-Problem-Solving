class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag = False
        left = 0
        right = 0
        max_val = 0
        
        while right < len(nums):
            if nums[right] == 0 and not flag:
                flag = True
            elif nums[right] == 0 and flag:
                max_val = max(max_val, (right - left) - 1)
                while nums[left] != 0:
                    left += 1
                left += 1
                
            right += 1
            
        max_val =max(max_val, (right - left) - 1)
        
        return max_val
            
                