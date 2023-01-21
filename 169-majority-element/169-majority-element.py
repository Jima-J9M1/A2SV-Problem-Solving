class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = math.ceil(len(nums)/2)
        
        for ele in set(nums):
            c  = nums.count(ele)
            
            if c >= val:
                return ele