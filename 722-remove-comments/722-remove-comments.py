class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        res = []
        buffer = ""
        isOpen = False
        
        for line in source:
            
            i = 0
            while i < len(line):
                
                if i < len(line) - 1 and line[i] == "/" and line[i + 1] == "/" and not isOpen:
                    i = len(line)
                elif i < len(line) - 1 and line[i] == "/" and line[i + 1] == '*' and not isOpen:
                    i += 1
                    isOpen = True
                elif i < len(line) - 1 and line[i] == "*" and line[i + 1] == "/" and isOpen:
                    isOpen = False
                    i += 1
                elif not isOpen:
                    buffer += line[i]
                i += 1
            
            if buffer and not isOpen:
                res.append(buffer)
                buffer = ""
        
        return res
                