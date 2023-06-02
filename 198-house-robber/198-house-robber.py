class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        memo = {}
        
    
        def dfs(indx):
            if indx not in memo:
                if indx >= len(nums):
                    return 0



                rob = dfs(indx + 2) + nums[indx]
                not_rob = dfs(indx + 1)


                memo[indx] = max(rob, not_rob)
            
            return memo[indx]
        
            
        ans = dfs(0)
        return ans
    
            
            
        