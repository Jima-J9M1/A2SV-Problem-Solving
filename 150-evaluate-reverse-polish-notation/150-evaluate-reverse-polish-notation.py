class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        right = 0
        op = {"+","/","-","*"}
        stack = []
        
        while right < len(tokens):
            if tokens[right] in op:
                if tokens[right] == "/":
                    a = stack.pop()
                    b = stack.pop()
                    val = int(b / a)
                    
                    stack.append(val)
                elif tokens[right] == "*":
                    a = stack.pop()
                    b = stack.pop()
                    val = a * b
                    
                    stack.append(val)
                elif tokens[right] == "-":
                    a = stack.pop()
                    b = stack.pop()
                    
                    val = b - a
                    
                    stack.append(val)
                elif tokens[right] == "+":
                    a = stack.pop()
                    b = stack.pop()
                    
                    val = a + b
                    stack.append(val)
            else:
                stack.append(int(tokens[right]))
            
            right += 1
                
        return stack[-1]