    def II():return int(input())
    def MI():return map(int, input().split())
    def LI():return list(map(int, input().split()))
    def LLI(rows_number): return [LI() for _ in range(rows_number)]
    def SI():return input()
    def LSI():return list(input())
    def LSI_():return [i for i in input().split()]
     
     
    def main():
        length = II()
        arr = LI()
        for indx in range(length):
            if indx == arr[indx] - 1:
                continue
     
            ele = arr[indx]
     
            i = 0
            while i < 3:
                if ele == arr[ele - 1]:
                    break
     
                ele = arr[ele-1]
                i += 1
     
     
     
            if i == 3 and ele == arr[indx]:
     
                print('YES')
                return
        print('NO')
     
    main()
