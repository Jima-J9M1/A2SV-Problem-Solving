class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        len_val = len(nums)/3
        res = []
        
        for ele in set(nums):
            val = nums.count(ele)
            
            if val > len_val:
                res.append(ele)
                
                
        return res