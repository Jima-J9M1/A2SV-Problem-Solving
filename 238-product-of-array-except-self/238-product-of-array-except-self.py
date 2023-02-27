class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_pro = [1] * (len(nums) + 1)
        suffix_pro = [1] * (len(nums) + 1)
        
        for i in range(1,len(prefix_pro)):
            prefix_pro[i] = prefix_pro[i - 1] * nums[i - 1]
        
        for i in range(len(suffix_pro) - 2, -1, -1):
            suffix_pro[i] = nums[i] * suffix_pro[i + 1] 
        
        
        res = [1] * (len(nums) + 1)
        for i in range(1,len(prefix_pro)):
            res[i] = prefix_pro[i - 1] * suffix_pro[i]
            
        return res[1:]
        