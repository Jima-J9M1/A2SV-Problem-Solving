class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)
        
        
        #point the first position and last positoin of the mountain find the middle of the mountain
        while left < right:
            mid = left + (right - left) // 2
            
            #check the peak of the moutain before and after is less than the middle one then return the peak of the mountain
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            
            #if the peak of the mountain before the middle of the mountain is greater than the middle of the mountain the change the last position to the middle one
            if arr[mid] <= arr[mid - 1]:
                right = mid
            
            #if the peak of the mountain after the middle of the mountain is greater than the middle of the mountain the change the last position to the middle one
            else:
                left = mid + 1
        
        return mid
                