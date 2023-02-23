class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        
        min_val =float("+inf")
        add = 0
        
        while right < len(nums):
            add += nums[right]
            
            while add >= target:
                min_val = min(min_val,right - left + 1)
                add -= nums[left]
                left += 1
            
            right += 1
        
        return min_val if min_val != float("+inf") else 0
                
            
            