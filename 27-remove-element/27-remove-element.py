class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        length = len(nums)
        index = 0
        while index < length:
            if nums[index] == val:
                nums.remove(nums[index])
                length -= 1
            else:
                index += 1
