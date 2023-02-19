class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        left = 0
        
        while left < len(s):
            
            if stack and s[left] == stack[-1]:
                stack.pop()
                left += 1
                continue
                
            stack.append(s[left])
            left += 1
        
        return "".join(stack)