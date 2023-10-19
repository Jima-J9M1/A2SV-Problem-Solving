class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        
        str1 = []
        str2 = []
        
        for ele in s:
            if str1 and ele == "#":
                str1.pop()
                continue
            
            if not str1 and ele == "#":
                continue
                
                
            else:str1.append(ele)
                
        for ele in t:
            if str2 and ele == "#":
                str2.pop()
                continue
            
            if not str2 and ele == "#":
                continue
                
            else:str2.append(ele)
                
                
            
        if str1 == str2:
            return True
        
        return False
            