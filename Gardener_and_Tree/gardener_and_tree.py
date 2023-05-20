from collections import deque,Counter,defaultdict
import heapq

import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def solve():
    
    edge,k = MI()
    # print(edge)
    graph = defaultdict(list)
    incoming = defaultdict(int)
    queue = deque()
    visited = set()


    for _ in range(edge - 1):
        v1, v2 = MI()
        graph[v1].append(v2)
        graph[v2].append(v1)
        incoming[v1] += 1
        incoming[v2] += 1

    # print(graph)
    for ele in range(1, edge + 1):
        if incoming[ele] == 0 or incoming[ele] == 1:
            queue.append(ele)
            visited.add(ele)

    ans = 0
 
    while queue and k > 0:
        len_level = len(queue)
        ans += len_level 


        
        for __ in range(len_level):
            
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    incoming[neighbor] -= 1

                    if incoming[neighbor] == 1:
                        queue.append(neighbor)
                        visited.add(neighbor)


        k -= 1

    res = edge - ans 

    print(res)
            


tastCase = II()

for __ in range(tastCase):
    input()
    solve()

  
