class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        nextGreater = [-1] * len(nums)
        stack = []
        
        
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] < nums[i]:
                stackTop = stack.pop()
                nextGreater[stackTop] = nums[i]
            
            stack.append(i)
        
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] < nums[i]:
                stackTop = stack.pop()
                nextGreater[stackTop] = nums[i]
            
            if not stack:
                break
                
        
        return nextGreater
                