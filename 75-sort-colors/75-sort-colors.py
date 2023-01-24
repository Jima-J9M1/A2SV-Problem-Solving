class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_ele = [0]*(4)
        
        for num in nums:
            count_ele[num] += 1
            
        target = 0
        
        for key,val in enumerate(count_ele):
            
            for i in range(val):
                nums[target] = key
                target += 1           

        return nums