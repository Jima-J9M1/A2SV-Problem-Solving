class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefx_sum = [0] * (len(nums) + 1)
        
        for i in range(0,len(nums)):
            prefx_sum[i + 1] = prefx_sum[i] + nums[i]
            
        return prefx_sum[1:]