class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        length = len(nums)
        
        #find the indices(plular of index) of target in nums          
        for index in range(length):
            if target == nums[index]:
                res.append(index)
        
        return res