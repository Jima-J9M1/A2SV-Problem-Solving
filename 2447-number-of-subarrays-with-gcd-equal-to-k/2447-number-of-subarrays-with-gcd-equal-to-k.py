class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            gcd_val = 0
            for j in range(i, len(nums)):
                gcd_val = math.gcd(gcd_val, nums[j])
                
                if gcd_val == k:
                    count += 1
                    
                elif gcd_val < k:
                    break        
                    
        return count
                
            
                
                
            
            
    
    