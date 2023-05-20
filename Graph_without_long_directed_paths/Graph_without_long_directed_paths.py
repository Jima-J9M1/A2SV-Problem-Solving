import heapq
from collections import deque, defaultdict
import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def LSI(): return list(map(str,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def solve():
    V,E = MI()
    graph = defaultdict(list)
    edge = []

    for i in range(E):
        v1, v2 = MI()
        edge.append((v1,v2))
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    visited = [0] * (V + 1)
    stack = [(1,1)]

    while stack:
        node, color = stack.pop()
        visited[node] = color
        

        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                stack.append((neighbor,-color))
                
            else:
                if visited[neighbor] == color:
                    print("NO")
                    return
    print("YES")
    for start,end in edge:
        print(1 if visited[start] == 1 else 0, end = "")


solve()
                

     
                
                
