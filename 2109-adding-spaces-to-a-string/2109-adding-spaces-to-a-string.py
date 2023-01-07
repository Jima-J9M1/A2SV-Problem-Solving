class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = s[:spaces[0]] + " "
        right = 0
        length = len(spaces)
        
        
        while right < length - 1:
            new_str += s[spaces[right]:spaces[right + 1]] + " "
            right += 1
            
        new_str += s[spaces[right]:]
        
        return new_str
            
        