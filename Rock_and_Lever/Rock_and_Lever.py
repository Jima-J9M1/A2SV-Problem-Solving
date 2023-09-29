collections import defaultdict
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
    
def bitMapp(num1):
    
    count = defaultdict(int)
    
    for i in num1:
        num = int.bit_length(i)
        count[num] += 1
    
    ans = 0
    for key in count:
        if count[key] > 1:
           
           ans += ((count[key] * (count[key] - 1))) // 2
           
           
    print(ans)
        
    
        
 
 
num2  = II()
 
for __ in range(num2):
    size = II()
    arr = LI()
    bitMapp(arr)
 
    
 
    
    
    
    
