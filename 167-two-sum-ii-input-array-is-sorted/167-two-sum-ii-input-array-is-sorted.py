class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            cal = numbers[left] + numbers[right]
            
            if cal < target:
                left += 1
            elif cal > target:
                right -= 1
            else:
                break
        
        return [left + 1, right + 1]