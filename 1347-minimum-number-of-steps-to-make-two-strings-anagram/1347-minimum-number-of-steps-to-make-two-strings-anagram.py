class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        
        count = 0
        
        for key in count_s:
            if key in count_t:
                count += (count_s[key] - count_t[key]) if count_s[key] >= count_t[key] else 0
            else:
                count += count_s[key]
                
                
        return count