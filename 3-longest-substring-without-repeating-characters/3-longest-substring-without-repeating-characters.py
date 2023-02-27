class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        dic = defaultdict(int)
        max_val = 1
        
        while right < len(s):
            
            while dic[s[right]] != 0:
                dic[s[left]] -= 1
                left += 1
                
            max_val = max(max_val,right - left + 1)
            
            dic[s[right]] += 1
            right += 1
        
        # if dic
        return max_val if s else 0
            