class Solution:
    def reverse(self, x: int) -> int:

        str_val = str(x)
        if x < 0:
            new_val = [str(x) for x in str_val[1:]]
            new_val = -int("".join(new_val[::-1]))
        else:
            new_val = [str(x) for x in str_val]
            new_val = int("".join(new_val[::-1]))
        
        
        if (-2)**31 >= new_val or new_val >= (2**31 - 1):
            return 0
        
        return int(new_val)
            
            