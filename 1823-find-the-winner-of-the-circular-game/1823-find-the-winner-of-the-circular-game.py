class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n + 1)]
        left = 0
        count = 0
        
        while len(players) > 1:
            count += 1
            
            if count == k:
                players.pop(left)
                count = 0
                continue
                
                
            n = len(players)
            left += 1
            left = left % n
            
            
        return players[-1]
            
            