from collections import deque
import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def solve():
    n = II()
    _dict = {}
    
    for i in range(1, int(n**0.5)+ 1):
        if math.gcd(i, n//i) == 1 and i * (n//i) == n:
            _dict[max(i,n//i)] = [i,n//i]
            
    
    print(*_dict[sorted(_dict)[0]])
    
 
