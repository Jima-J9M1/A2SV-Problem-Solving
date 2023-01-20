class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        index  = length - 2
        
        if length == 1:
            return [-1]
        
        max_val = arr[index + 1]
        
        #Find the largest element to the right of index's and replace it
        while index  >= 0:
            temp = max_val
            if arr[index] > max_val:
                max_val = arr[index]
                
            arr[index] = temp
                
            index -= 1  
            
        arr[-1] = -1
                
        return arr
            