class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        count_t = Counter(t)
        count = 0
        
        left = 0
        right = 0
        count = 0
        res = [-1,-1]
        min_val = float("+inf")
        
        while right < len(s):
            
            window[s[right]] = 1 + window.get(s[right],0)
            
            if s[right] in count_t and window[s[right]] == count_t[s[right]]:
                count += 1
                
            while count == len(count_t):
                
                if (right - left + 1) < min_val:
                    res = [left,right]
                    min_val = right - left + 1
                    
                window[s[left]] -= 1
                
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    count -= 1
                    
                left += 1
            
            right += 1
        
        ans = s[res[0]:res[1] + 1]
        
        return ans if min_val != float("+inf") else ""
        
                