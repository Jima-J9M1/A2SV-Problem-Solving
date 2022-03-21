class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            end= len(nums) - 1
            while i != end:
                if nums[i] + nums[end] == target:
                    res.append(i)
                    res.append(end)
                end -= 1
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             res.append(i)
        #             res.append(j)
                    
        return res
