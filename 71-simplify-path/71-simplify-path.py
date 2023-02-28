class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []
        
        for i in s:
            if i == "" or i == ".":
                continue
            if stack and i == "..":
                stack.pop()
            elif i == "..":
                continue
            else:
                stack.append(i)
                
        return '/' +'/'.join(stack)
