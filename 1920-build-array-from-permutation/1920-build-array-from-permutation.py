class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        
        for index in range(length):
            ans.append(nums[nums[index]])
        
        return ans