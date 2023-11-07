class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(indx, ans):
            res.append(ans[:])
            
            if indx >= len(nums):
                return
            
            for i in range(indx, len(nums)):
                backtrack(i + 1, ans + [nums[i]])
                
            return
        
        
        ans = []
        backtrack(0, ans)
            
        
        return res