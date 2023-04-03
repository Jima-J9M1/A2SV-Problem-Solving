class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        

        def check(num):
            #
            total = 0
                
            for ele in nums:
                    
                total += (math.ceil(ele / num))
                              
                if total > threshold:
                    return False
                
            return True
                        
        
        #binary search
        left = 1
        right = max(nums)
                        
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            
            else:
                left = mid + 1
            
        return left
            