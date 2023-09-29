def II():return int(input())
def MI():return map(int, input().split())
def LI():return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI():return input()
def LSI():return list(input())
def LSI_():return [i for i in input().split()]
 
def prime(num):
    res = []
    d = 2
 
    while d * d <= num:
        if num % d == 0:
            res.append(d)
            num //= d
            continue
 
        d += 1
 
    if num > 2:
        res.append(num)
    
    return res
 
 
def main():
    num = II()
    prices = [x + 1 for x in range(1, num + 1)]
    color = [1 for x in range(1,num + 1)]
    prime_res = []
 
    if num <= 2:
        print(1)
        print(*([1] * num))
    else:
        print(2)
        
        for x in prices:
 
            prime_res = prime(x)
 
            for ele in prime_res:
                color[ele - 2] = 2
 
        print(*color)
 
    
 
main()
