class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        split_word = haystack.replace(needle, "0")
        
        for i in range(len(split_word)):
            if split_word[i] == '0':
                return i
                
                
        return -1