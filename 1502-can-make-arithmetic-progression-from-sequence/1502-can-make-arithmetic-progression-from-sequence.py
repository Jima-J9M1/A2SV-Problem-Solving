class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff_val = arr[0] - arr[1]
        flag = True
        
        for i in range(len(arr) - 1):
            diff = arr[i] - arr[i + 1]
            if diff != diff_val:
                flag = False
                break
                
        return flag
                
            