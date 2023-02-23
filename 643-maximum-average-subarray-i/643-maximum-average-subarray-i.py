class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avr = float("-inf")
        
        left = 0
        right = 0
        
        add = 0
        
        while right < len(nums):
            add += nums[right]
            
            if (right - left + 1) == k:
                max_avr = max(max_avr, add/k)
                add -= nums[left]
                left += 1
            
            right += 1
        
        
        return max_avr