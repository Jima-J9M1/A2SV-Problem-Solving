class Solution:
    def reverseWords(self, s: str) -> str:
        flag = 0
        res = ""
        for i in range(len(s)):
            if s[i] == " ":
                res += s[flag:i][::-1] + " "
                flag = i + 1
        
        res += s[flag:][::-1]
        
        return res