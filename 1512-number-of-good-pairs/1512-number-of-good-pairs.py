class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count_pairs = 0
        _dict = {}
        
        for val in nums:
            
            if val in _dict:
                _dict[val] += 1
            else:
                _dict[val] = 1
        
        for key in _dict:
            
            val = _dict[key]
            
            for indx in range(val):
                count_pairs += indx
                
        return count_pairs
                
        
        
        
#         count = 0
#         length = len(nums)
        
#         for index in range(length):
#             left = index + 1
            
#             while left < length:
                
#                 if nums[index] == nums[left]:
#                     count += 1
#                 left += 1
                
#         return count