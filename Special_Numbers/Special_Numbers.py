I():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def bit_map(base, pos):
   i = 0
   ans = 0
   length = int.bit_length(pos)
   
   while i < length:
       shift = 1 << i
       
       val = pos & shift
  
       if val > 0:
           ans += base ** i
           
       i += 1
    
   return ans
testcases = II()
 
for __ in range(testcases):
    base, pos = MI()
    
    ans = bit_map(base, pos)
    print(ans % (10**9 + 7))
 
    
 
    
    
