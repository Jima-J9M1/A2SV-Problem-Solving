class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        str_val = [str(x) for x in digits]
        num = int("".join(str_val)) + 1
        num = str(num)
        res = [int(x) for x in num]
        
        return res