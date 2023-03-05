class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        left = 0
        right = x
        ans = 0
        
        # check if the sqaure root of x number is bellow middle of x or above middle of x
        while left < right:
            mid = left + (right - left) // 2
            
            #check if the middle number square is less than x number so increase our left pointer to next and add one two it
            #store the middle value cause it maybe the answer of x number because it was written by integer
            if x >= mid * mid:
                left = mid + 1
                ans = mid
            
            #check if the middle element is above the x number 
            elif x < mid * mid:
                right = mid
            else:
                ans = mid
                break
            
        return ans