class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        
        for char in s:
            
            if char == "(":
                stack.append(char)
             
            else:
                score = 0
                while stack and stack[-1] != "(":
                    val = stack.pop()
                    score += val
                
                stack.pop()
                if score:
                    stack.append(score * 2)
                else:
                    stack.append(1)
        
            
        return sum(stack)
      