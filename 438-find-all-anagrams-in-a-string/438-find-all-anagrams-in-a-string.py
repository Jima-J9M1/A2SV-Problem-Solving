class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        
        len_p = len(p)
        res = []
        
        for i in range(len(s) - len_p + 1):
            count_s = Counter(s[i:i + len_p])
            
            if count_s == count_p:
                res.append(i)
            
            
        
        return res