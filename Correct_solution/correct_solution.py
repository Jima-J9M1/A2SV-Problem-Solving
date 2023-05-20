from collections import deque,Counter
import heapq

import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def solve():
    alice_num = list(input())
    bob_num = input()
    heapq.heapify(alice_num)
    
    zero = -1
    ans = []
    while alice_num:
        ans.append(heapq.heappop(alice_num))
        
        if ans[-1] == "0":
            zero = len(ans)-1
            
    if zero != -1 and zero + 1 < len(ans):
        ans[0], ans[zero+1] = ans[zero+1], ans[0]
                
    ans = "".join(ans)
    if ans != bob_num:
        print("WRONG_ANSWER")
        
    else:
        print("OK")
    
   
        

solve()

        
