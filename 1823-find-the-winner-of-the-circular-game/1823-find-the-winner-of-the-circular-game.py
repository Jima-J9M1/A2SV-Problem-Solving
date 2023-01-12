class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friend_num = [num for num in range(1,n + 1) ]
        left = 0
        count = 0

        while len(friend_num) > 1:
            count += 1
            
            if count == k:
                friend_num.pop(left)
                count = 0
                continue

            n = len(friend_num)
            left += 1
            left = left % n
        
        
        return friend_num[-1]
                