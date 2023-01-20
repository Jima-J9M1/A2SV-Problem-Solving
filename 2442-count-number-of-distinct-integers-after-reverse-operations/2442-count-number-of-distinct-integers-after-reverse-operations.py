class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        
        for index in range(length):
            
            val = str(nums[index])
            nums.append(int(val[::-1]))
        
        return len(set(nums))
            