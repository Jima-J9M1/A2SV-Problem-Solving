class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = x
        if x < 0:return False
        num = 0
        while x > 0:
            rem = x % 10
            num = (num * 10) + rem
            x = x // 10
        if num == ans:
            return True
        return False
            