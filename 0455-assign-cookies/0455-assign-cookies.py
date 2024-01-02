class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr1 = len(g) - 1
        ptr2 = len(s) - 1
        g.sort()
        s.sort()
        count = 0
        
        while ptr1 >= 0 and ptr2 >= 0:
            if g[ptr1] <= s[ptr2]:
                ptr1 -= 1
                ptr2 -= 1
                count += 1
            else:
                ptr1 -= 1
                
        return count
            