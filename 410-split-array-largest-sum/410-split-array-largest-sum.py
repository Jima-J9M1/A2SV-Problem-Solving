class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(min_val):
            split = 1
            total_sum = 0
            
            for ele in nums:
                total_sum += ele
                
                if total_sum > min_val:
                    total_sum = ele
                    split += 1
                    if split > k:
                        return False
                
            return True
        
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            if check(mid):
                right = mid
            
            else:
                left = mid + 1
                
        return left