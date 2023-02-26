class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = defaultdict(int)
        left = 0
        right = 0
        max_val = 0
        
        while right < len(s):
            dic[s[right]] += 1
            
            while dic and (right - left + 1) - max(dic.values()) > k:
                max_val = max(max_val, right - left)
                dic[s[left]] -= 1
                left += 1
                
            
            right += 1
        
        max_val = max(max_val,right - left)
        
        return max_val