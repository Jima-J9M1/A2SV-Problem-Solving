class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(p)
        length = len(s)
        count_p = Counter(p)
        res = []
        
        for i in range(length - size + 1):
            count_s = Counter(s[i:i + size])
            
            if count_p == count_s:
                res.append(i)
                
        return res
                
            