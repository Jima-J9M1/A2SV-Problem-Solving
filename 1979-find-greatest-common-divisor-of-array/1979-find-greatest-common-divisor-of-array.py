class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1 = max(nums)
        num2 = min(nums)
        
        ans = self.gcd(num1, num2)
        
        return ans
    
    def gcd(self, num1,num2):
        if num2 == 0:
            return num1
        
        
        return self.gcd(min(num1, num2), max(num1, num2) % min(num1, num2))
    
        