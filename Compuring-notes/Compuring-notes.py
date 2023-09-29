from collections import deque,Counter,defaultdict
import heapq
 
import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
 
def solve():
    AAIT = input()
    AASTU = input()
    left = 0
    right = len(AAIT) - 1
    indx = [float("+inf"), -1]
 
    while right >= 0 and left < len(AAIT):
        if AAIT[left] == "-" and indx[0] == float("+inf"):
            indx[0] = left
        
        if AAIT[right] == "-" and indx[1] == -1:
            indx[1] = right
 
        right -= 1
        left += 1
 
    left = 0
    right = len(AASTU) - 1
 
    indx2 = [float("+inf"),-1]
 
    while right >= 0 and left < len(AASTU):
        if AASTU[left] == "-" and indx2[0] == float("+inf"):
            indx2[0] = left
        
        if AASTU[right] == "-" and indx2[1] == -1:
            indx2[1] = right
 
        right -= 1
        left += 1
 
    left_min = min(indx[0],indx2[0])
    right_max = max(indx[1],indx2[1])
    flag = True
    for i in range(left_min):
        if AAIT[i] != AASTU[i]:
            flag = False
            break
 
    flag2 = True
    right_max += 1
 
 
    while right_max < len(AAIT) and right_max < len(AASTU):
        if AAIT[right_max] != AASTU[right_max]:
            flag2 = False
            break
 
        right_max += 1
 
    if flag and flag2:
        print("YES")
    else:
        print("NO")
 
solve();
 
