class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #count the number of zero's in nums
        size_zero = nums.count(0)
        
        length = len(nums)
        
        if length == 1 or size_zero == 0:
            return nums
        
        index = 0
        count = 0
        while count <= size_zero and index < length:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                count += 1
            else:
                index += 1
        