class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)
        
        

        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            

            if arr[mid] <= arr[mid - 1]:
                right = mid
            

            else:
                left = mid + 1
        
        return mid
                