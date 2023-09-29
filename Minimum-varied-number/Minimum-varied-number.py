    from collections import deque,Counter,defaultdict
    import heapq
     
    import math
     
    def II():return int(input())
    def LI(): return list(map(int,input().split()))
    def MI(): return map(int,input().split())
    def SI(): return sorted(list(map(int,input().split())))
     
     
     
    def solve():
        n = II()
     
        pattern = {10:9,18:8,25:7,31:6,36:5,40:4,43:3,45:2}
        start = 0
     
        if n / 10 < 1:
            print(n)
            return 
        
        for key in pattern:
            if n >= key:
                start = key
            if n < key:
                break
        # print(start)
        start_pt = n - start
        arr = [str(start_pt + 1)]
     
        for i in range(pattern[start],10):
            arr.append(str(i))
     
        print("".join(arr))
     
    tasteCase = II()
     
    for _ in range(tasteCase):
        solve()
     
