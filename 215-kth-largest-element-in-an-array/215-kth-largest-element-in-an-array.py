class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            
            pivot = arr[0]
            left = []
            right = []
            
            for indx in range(1, len(arr)):
                if arr[indx] < pivot:
                    left.append(arr[indx])
                    
                else:
                    right.append(arr[indx])
                    
            return quickSort(left) + [pivot] + quickSort(right)
        
        
        sort_val = quickSort(nums)
        
        return sort_val[-k]