class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        _dict = Counter(s)
        res = ""
        ans = []
        count = 0
        
        for ele in s:
            _dict[ele] -= 1
            if _dict[ele] == 0:
                count += 1
            res += ele
            
            if len(set(res)) == count:
                ans.append(len(res))
                res = ""
                count = 0
        
        return ans