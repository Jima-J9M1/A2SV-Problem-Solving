I():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
    
def bitMapp(num1):
    count = 0
    while num1 > 1:
        num2 = 1 << int.bit_length(num1) - 1
        num1 -= num2
        count += 1
        
    if num1 == 1:
        print(count + 1)
    else:
        print(count)
    
        
 
 
num2  = II()
 
bitMapp(num2)
    
 
    
