    from collections import deque
    import math
     
    def II():return int(input())
    def LI(): return list(map(int,input().split()))
    def MI(): return map(int,input().split())
    def SI(): return sorted(list(map(int,input().split())))
     
    def solve():
        solider, player, k = MI()
        arr = []
        for __ in range(player + 1):
            arr.append(II())
        
        friends = 0
     
        for index in range(player):
            fedor = arr[-1]
            count = 0
            while fedor != 0 or arr[index] != 0:
                if (fedor & 1) != (arr[index] & 1):
                    count += 1
     
                fedor >>= 1
                arr[index] >>= 1
            
            if count <= k:
                friends += 1
     
     
        print(friends)
     
    solve()
