    from collections import deque,Counter,defaultdict
    import heapq
     
    import math
     
    def II():return int(input())
    def LI(): return list(map(int,input().split()))
    def MI(): return map(int,input().split())
    def SI(): return sorted(list(map(int,input().split())))
     
     
    def helper(n, num, pattern):
        ptr = n - 1
        ans = 0
     
        while ptr >= 0 and num[ptr] != pattern[1]:
            ptr -= 1
            ans += 1
        
        ptr -= 1
        while ptr >= 0 and num[ptr] != pattern[0]:
            ptr -= 1
            ans += 1
        
        return ans
     
            
     
     
     
    def solve():
        arr = input()
        array = ['00','25','50','75']
        ans = float('+inf')
        for i in range(len(array)):
            res = helper(len(arr), arr, array[i])
            
            ans = min(res, ans)
        
        print(ans)
     
    tastCase = II()
     
    for _ in range(tastCase):
        solve()
