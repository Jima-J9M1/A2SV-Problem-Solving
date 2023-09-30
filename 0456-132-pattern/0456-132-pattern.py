class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        patter_1 = [0]*len(nums)
        min_val = float("inf")
        mono_stack = []
        
        
        for i in range(len(nums)):
            min_val = min(min_val, nums[i])
            patter_1[i] = min_val
            
            
            
        for i in range(len(nums)):
            
            while mono_stack and nums[mono_stack[-1]] < nums[i]:
                mono_stack.pop()
                
            if mono_stack:
                pt_1 = patter_1[mono_stack[-1]]
                pt_2 = nums[i]
                pt_3 = nums[mono_stack[-1]]
                
                if pt_1 < pt_2 < pt_3:
                    return True
                
            mono_stack.append(i)
            
            
        return False