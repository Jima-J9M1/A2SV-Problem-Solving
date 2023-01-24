class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        num_set = set()
        length = len(numbers)
        left = 0
        
        while left < length:
            if target - numbers[left] in num_set:
                break
            
            num_set.add(numbers[left])
            left += 1
        
        indx = numbers.index(target - numbers[left])
        
        return [indx + 1, left+ 1]