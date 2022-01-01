class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lists=[];
        nums=sorted(nums)
        for i in range(len(nums)):
            if target ==nums[i]:
                lists.append(i)
        return lists
        
