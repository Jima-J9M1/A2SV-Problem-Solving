    from collections import deque, defaultdict
    import math
     
    def II():return int(input())
    def LI(): return list(map(int,input().split()))
    def LSI(): return list(map(str,input().split()))
    def MI(): return map(int,input().split())
    def SI(): return sorted(list(map(int,input().split())))
     
    def dfs( graph, start, visited,res):
        stack = [start]
        
        while stack:
            node = stack.pop()
            res.append(node)
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node] - visited)
            
            # print(stack)
             
     
     
        
    def solve():
        len_stamps = II()
        graph = defaultdict(set)
        for _ in range(len_stamps):
            city1, city2 = MI()
            graph[city1].add(city2)
            graph[city2].add(city1)
     
        for key in graph:
            if len(graph[key]) == 1:
                ans = key
        
        visited = set()
        res = []
        dfs(graph,ans,visited,res)
     
        print(*res)
     
            
    solve()
