    from collections import deque,Counter,defaultdict
    import heapq
     
    import math
     
    def II():return int(input())
    def LI(): return list(map(int,input().split()))
    def MI(): return map(int,input().split())
    def SI(): return sorted(list(map(int,input().split())))
     
     
     
    def solve():
        n = II()
        mati = LI()
        ibsa = LI()
        
        mati.sort()
        ibsa.sort()
     
        mati_score = 0
        ibsa_score = 0
        ptr1 = n - 1
        ptr2 = n - 1
        count = 0
     
        while ptr1 < n and ptr2 >= 0 and count < n:
            if mati[ptr2] > ibsa[ptr1]:
                mati_score += 1
                ptr2 -= 1
     
            else:
                ibsa_score += 1
                ptr2 -= 1
                ptr1 -= 1
     
            count += 1
        print(math.ceil((mati_score)/2))
     
     
    solve()
