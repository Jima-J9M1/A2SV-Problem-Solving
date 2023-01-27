class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        num1 = 0
        num2 = 0 
        ans = False
        while (num1**2) <= c:
            num2 = math.sqrt(c - num1**2)
            if math.ceil(num2) == math.floor(num2):
                ans = True
                break
                
            num1 += 1
        
        return ans