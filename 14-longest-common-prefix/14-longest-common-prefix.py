class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_val = float ("inf")
        str_ans = ""
        left = 0
        flag = 0
        
        for str_val in strs:
            min_val = min(min_val, len(str_val))
        
        for ind in range(min_val):
            res = strs[0][left]
            for i in range(1,len(strs)):
                if res != strs[i][left]:
                    return str_ans
            str_ans += res
            left += 1
            
        return str_ans
                
            
            
            