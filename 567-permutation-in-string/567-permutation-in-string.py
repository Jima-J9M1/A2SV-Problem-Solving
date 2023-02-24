class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s = len(s1)
        count_s = Counter(s1)
        ans = False
        left = 0
        right = 0
        
        while right < len(s2):
            
            if (right - left + 1) == len(s1):
                count_p = Counter(s2[left:right+1])
                if count_p == count_s:
                    ans = True
                    break
                left += 1
                
            right += 1
                    
                    
        return ans
            