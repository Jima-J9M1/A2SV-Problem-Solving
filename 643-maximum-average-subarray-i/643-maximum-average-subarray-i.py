class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avr = float("-inf")
        left = 0
        right = 0
        avr = 0
        while right < len(nums):
            avr += nums[right] 
            
            if (right - left + 1) == k:
                max_avr = max(max_avr,(avr / k))
                avr -= nums[left]
                left += 1
                
            right += 1
            
        
        return max_avr
                