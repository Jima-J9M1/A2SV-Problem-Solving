class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        dp = {}
        
        
        
        
        for i in range(len(nums)):
            
            for j in range(i + 1, len(nums)):
                
                diff = nums[j] - nums[i]
                
                if (diff, i) in dp:
                    dp[(diff, j)] = dp[(diff, i)] + 1
                    
                else:
                    
                    dp[(diff, j)] = 2
                    
                
                
        val = dp.values()
        return max(dp.values())