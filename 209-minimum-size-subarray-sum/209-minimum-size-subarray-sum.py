class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_result = 0
        min_val = float("inf")
        
        while right < len(nums):
            sum_result += nums[right]
            
            while left <= right and sum_result >= target:
                min_val = min(min_val, (right - left + 1))
                sum_result -= nums[left]
                left += 1
                    
            right += 1
                    
        return min_val if min_val != float("inf") else 0
                    
                    
                    

                
                
        
        