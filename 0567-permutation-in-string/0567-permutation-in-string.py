class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        count_s1 = Counter(s1)
        right = 0
        ans = False
        
        while right < len(s2) - (n - 1):
            count_s2 = Counter(s2[right:right + n])
            if count_s2 == count_s1:
                ans = True
                break
                
            right += 1
                
                
                
        return ans
        