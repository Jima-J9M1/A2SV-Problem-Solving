class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        prevSmaller = [-1] * len(nums)
        prevSmaller[0] = nums[0]
        min_val = float("inf")
        
        
        for i in range(len(nums)):
            min_val = min(nums[i], min_val)
            prevSmaller[i] = min_val
            
        
        stack = []
        ans = False
        
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            if stack:
                a = prevSmaller[stack[-1]]
                c = nums[i]
                b = nums[stack[-1]]
                
                if a < c < b:
                    ans = True
                    break
                    
            stack.append(i)
            
        return ans
                
            
                
         