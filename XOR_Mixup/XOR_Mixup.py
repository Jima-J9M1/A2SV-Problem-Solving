int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
    
def bitMapp(num1):
    res = set(num1)
    
    if len(res) == 2  and 0 in res:
        print(0)
    elif len(res) >= 2 or len(res)== 1:
        print(num1[1])
 
        
testcases = II()
 
for i in range(testcases):
    length = II()
    num2  = LI()
    
    bitMapp(num2)
    
 
    
    
    
    
    
