    from collections import deque,Counter,defaultdict
    import heapq
     
    import math
     
    def II():return int(input())
    def LI(): return list(map(int,input().split()))
    def MI(): return map(int,input().split())
    def SI(): return sorted(list(map(int,input().split())))
     
    def solve():
        vertex,edge = MI()
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for _ in range(edge): 
            v1,v2 = MI()
            graph[v1].append(v2)
            graph[v2].append(v1)
            incoming[v1] += 1
            incoming[v2] += 1
        
        queue = deque()
        for key in incoming:
            if incoming[key] == 1:
                queue.append(key)
     
        k = 0 
        ans = []
        while queue and k < 2:
            len_level =  len(queue)
            ans.append(len_level)
            for _ in range(len_level):
                node = queue.popleft()
     
                for child in graph[node]:
                    incoming[child] -= 1
     
                    if incoming[child] == 1:
                        queue.append(child)
     
            k += 1
     
        print(ans[1], ans[0] // ans[1])
        # print(queue)
     
     
    tastCase = II()
    for _ in range(tastCase):
        solve()
