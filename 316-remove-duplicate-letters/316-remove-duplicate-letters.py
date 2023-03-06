class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #Count the frequency of the character in stirng
        count = Counter(s)
        #store the lexicographical order it means a string that is written in their order
        stack = []
        alpha = set()
        
        for indx in range(len(s)):
            
            while stack and s[indx] not in stack and stack[-1] >= s[indx] and count[stack[-1]] > 0:
                val = stack.pop()
                alpha.remove(val)
                
            
            
            if s[indx] not in alpha:
                stack.append(s[indx])
                alpha.add(s[indx])
                
            count[s[indx]] -= 1
        
        
        return "".join(stack)
            
        
        
        