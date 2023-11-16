class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        min_values = defaultdict(int)
        min_val = float('inf')
        
        for i in range(len(nums)):
            min_val = min(nums[i], min_val)
            min_values[nums[i]] = min_val
                
          
        stack = []
        for i in range(len(nums)):
            
            while stack and stack[-1] < nums[i]:
                stack.pop()
                
            if stack:
                num2 = stack[-1]
                num1 = min_values[num2]
                
                if num1 < nums[i] < num2:
                    return True
                
            stack.append(nums[i])
                
                
            
        return False
            
            