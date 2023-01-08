class Solution:
    def printVertically(self, s: str) -> List[str]:
        new_st = s.split()
        max_val = 0
        length = len(new_st)
        res = []
        
        for index in range(length):
            if len(new_st[index]) > max_val:
                max_val = len(new_st[index])
        
        
        for index in range(max_val):
            ans = ""
            for j in range(length):
                if index > len(new_st[j]) - 1:
                    ans+=" "
                    continue
                ans += new_st[j][index]
            res.append(ans)
        
        for index in range(len(res)):
            res[index] = res[index].rstrip()
            # print(ele.rstrip() + "/")
        
        return res
                
        