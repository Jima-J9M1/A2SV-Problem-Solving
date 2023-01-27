class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        pref_sqr = (num ** 0.5)
        
        if math.ceil(pref_sqr) == math.floor(pref_sqr):
            return True
        
        return False
        