class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_t = Counter(t)
        count_s = Counter(s)
        
        res = False
        
        if count_t == count_s:
            res = True
        
        
        return res