class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        
        self.backTracking(nums, [], 0)
        
        return self.ans
    
    def backTracking(self, nums, subset,idx):
        if len(subset) >= len(nums):
            return 
        
        
        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self.ans.append(subset[:])
            self.backTracking(nums, subset, i + 1)
            subset.pop()
            
            
            
            