class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        _dict = {}
        index = 0
        length = len(numbers)
        
        while index < length:
            if target - numbers[index] in _dict:
                break
                
            _dict[numbers[index]] = index
            index += 1
        
        val = _dict[target - numbers[index]]
        
        return [val + 1, index + 1]
        
        
        
        
        
        
#         num_set = set()
#         length = len(numbers)
#         left = 0
        
#         while left < length:
#             if target - numbers[left] in num_set:
#                 break
            
#             num_set.add(numbers[left])
#             left += 1
        
#         indx = numbers.index(target - numbers[left])
        
#         return [indx + 1, left+ 1]