class Solution:
    def maximum69Number (self, num: int) -> int:
        
        str_val = list(str(num))
        left = 0
        
        for i in range(len(str_val)):
            if str_val[i] == "6":
                str_val[i] = "9"
                break
            
        return int("".join(str_val))