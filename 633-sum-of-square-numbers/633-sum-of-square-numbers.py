class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ptr = int(c**0.5)
        left = 0
        right = ptr
        res = 0
        
        while left <= right:
            res = left **2 + right**2
            if res == c:
                return True
            if res < c:
                left += 1
            elif res > c:
                right -= 1
        return False
        
#         num1 = 0
#         num2 = 0 
#         ans = False
        
#         while (num1**2) <= c:
#             num2 = math.sqrt(c - num1**2)
#             if math.ceil(num2) == math.floor(num2):
#                 ans = True
#                 break
                
#             num1 += 1
        
#         return ans