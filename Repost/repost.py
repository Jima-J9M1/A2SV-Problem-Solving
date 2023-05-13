    from collections import deque, defaultdict
    import math
     
    def II():return int(input())
    def LI(): return list(map(int,input().split()))
    def LSI(): return list(map(str,input().split()))
    def MI(): return map(int,input().split())
    def SI(): return sorted(list(map(int,input().split())))
     
    def solve():
        len_post = II()
        queue = deque(['polycarp'])
        graph = defaultdict(list)
        level = 0
     
        for __ in range(len_post):
            post = LSI()
            graph[post[2].lower()].append(post[0].lower())
     
        while queue:
            len_level = len(queue)
     
            for _ in range(len_level):
            
                repost = queue.popleft()
     
                for neighbor in graph[repost]:
                    queue.append(neighbor)
     
            level += 1
        
        print(level)
     
    solve()
