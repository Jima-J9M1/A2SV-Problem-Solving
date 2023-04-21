class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        _dict = defaultdict(int)
        max_val = 0
        self.backTracking(nums, 0, _dict, 0,[])
        
        for key in _dict:
            
            max_val = max(max_val, _dict[key])
            
        return max_val
    def backTracking(self, nums, idx, _dict, current_bitwise, path):
        if len(nums) < idx:
            return
        
        _dict[current_bitwise] += 1
        for i in range(idx, len(nums)):
            self.backTracking(nums, i + 1, _dict, current_bitwise | nums[i], path + [nums[i]])
            
            
            
        return
            
        