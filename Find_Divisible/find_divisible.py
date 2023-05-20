import heapq
from collections import deque, defaultdict
import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def LSI(): return list(map(str,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def solve():
    l, r = MI()

    print(l, l*2)


tastCase = II()

for __ in range(tastCase):
    solve()
