class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        ptr = 0
        
        while ptr < len(s):
            if stack and stack[-1][0] == s[ptr] and stack[-1][1] == k - 1:
                for i in range(k - 1):
                    stack.pop()
                    
                    
            else:
                if stack and stack[-1][0] == s[ptr]:
                    stack.append((s[ptr], stack[-1][1] + 1))
                else:
                    stack.append((s[ptr], 1))
                
            ptr += 1
            
        res = ""
        
        for ele in stack:
            res += ele[0]
            
            
        return res
        