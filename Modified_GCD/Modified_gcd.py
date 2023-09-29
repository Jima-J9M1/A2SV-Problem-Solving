

    from collections import defaultdict
    def II():return int(input())
    def MI():return map(int, input().split())
    def LI():return list(map(int, input().split()))
    def LLI(rows_number): return [LI() for _ in range(rows_number)]
    def SI():return input()
    def LSI():return list(input())
    def LSI():return [i for i in input().split()]
     
    def main():
        a,b = MI()
        n = II()
        ans = factorzation(a)
        ans_2 = factorzation(b)
        common_factors = ans_2.intersection(ans)
        c_f = sorted(list(common_factors))
        
        for _ in range(n):
            range_1, range_2 = MI()
            ans = binary_search(range_1, range_2, c_f, 0, len(c_f) - 1)
            print(ans)
     
    def binary_search(range_1, range_2, c_f, left, right):
        while left <= right:
     
            mid = left + (right - left) // 2
     
            if c_f[mid] > range_2:
                right = mid - 1
                
            else:
                left = mid + 1
                
        if c_f[right] >= range_1:
            return c_f[right]
        else:
            return -1
     
     
     
     
    def factorzation(n):
        res = set()
        for i in range(1, int(n**0.5) + 1):
            if i * (n//i) == n:
                res.add(i)
                res.add(n//i)
        
        return res
     
    main()
