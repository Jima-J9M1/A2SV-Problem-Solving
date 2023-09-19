class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        bitmask = 0
        
        for num in nums:
            shift = 1 << num


            if bitmask & shift > 0:
                return num
            
            bitmask |= shift
            
            