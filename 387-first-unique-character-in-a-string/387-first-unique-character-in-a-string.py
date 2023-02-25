class Solution:
    def firstUniqChar(self, s: str) -> int:
        list_s = list(s)
        
        count = Counter(list_s)
        ans = -1
        
        for i,val in enumerate(s):
            if count[val] == 1:
                ans = i
                break
        
        return ans