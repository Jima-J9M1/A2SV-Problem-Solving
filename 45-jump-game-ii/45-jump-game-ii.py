class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0
        ptr1 = 0 
        ptr2 = 0
        
        for i in range(len(nums) - 1):
            
            ptr1 = max(ptr1, i + nums[i])
            
            if i == ptr2:
                res += 1
                ptr2 = ptr1
            
        return res
            