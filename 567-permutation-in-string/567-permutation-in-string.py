class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _dict = defaultdict(int)
        left = 0
        right = 0
        len_s = len(s1)
        count = Counter(s1)
        ans = False
        
        while right < len(s2):
            if (right - left) == len_s:
                
                if count == _dict:
                    ans = True
                    break
                    
                _dict[s2[left]] -= 1
                
                if _dict[s2[left]] == 0:
                    del _dict[s2[left]]
                         
                left += 1
                
            _dict[s2[right]] += 1
            
            right += 1
            
        if (right - left) == len_s:
            if count == _dict:
                ans = True
            
        
        return ans