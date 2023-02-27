class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)
        right  = 0
        
        while right < len(shifts):
            l,r,k = shifts[right]
            
            if k == 0:
                prefix_sum[l] -= 1
                prefix_sum[r + 1] += 1
            else:
                prefix_sum[l] += 1
                prefix_sum[r + 1] -= 1
            
            right += 1
        
        alpahbet = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
            
        
        res = ""
        for i in range(len(s)):
            
            new_val = (((ord(s[i]) + prefix_sum[i]) - 97) % 26) + 97
            
            res += chr(new_val)
        
        
            
            
        return res
            