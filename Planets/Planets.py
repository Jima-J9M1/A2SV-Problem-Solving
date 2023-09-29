from collections import deque,Counter,defaultdict
import heapq
 
import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def solve():
    n, c = MI()
    arr = LI()
 
 
    graph = defaultdict(list)
 
    for indx, ele in enumerate(arr):
        graph[ele].append(indx)
 
    ans = 0
 
    for ele in graph:
        cost = len(graph[ele])
        real_cost = min(cost, c)
 
        ans += real_cost
 
    print(ans)
 
tasteCase = II()
 
for __ in range(tasteCase):
    solve()
    
