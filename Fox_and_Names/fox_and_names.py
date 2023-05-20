from collections import deque,Counter,defaultdict
import heapq

import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def solve():
    let = defaultdict(list)
    n = II()
    arr = []
    visited = set()
    indegree = defaultdict(int)
    queue = deque()

    for __ in range(n):
        arr.append(input())

    for indx in range(n - 1):
        min_val = min(len(arr[indx]), len(arr[indx + 1]))
        check = True

        for i  in range(min_val):
            if arr[indx][i] !=  arr[indx + 1][i]:
                let[arr[indx][i]].append(arr[indx + 1][i])
                indegree[arr[indx + 1][i]] += 1
                check = False
                break

        if check and len(arr[indx + 1]) < len(arr[indx]):
                print("Impossible")
                return 
    
    for  i in range(26):
        if indegree[chr(i + 97)] == 0:
            queue.append(chr(i + 97))
    s = ""

    while queue:
        node = queue.popleft()
        s += node
        for neighbor in let[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)
            

    if len(s) != 26:
        print("Impossible")
    else:
        print(s)


solve()
