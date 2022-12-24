class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for index in range(len(nums)):
            if nums[index] % 2 == 0:
                ans.insert(0,nums[index])
            else:
                ans.append(nums[index])
        
        return ans