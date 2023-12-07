class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_odd_val = 0
        indx = -1
        
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                indx = i
                break
                
            
                
                
        return num[ : indx + 1]