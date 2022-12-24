class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr) - 1
        index = 0
        while index < length + 1:
            if arr[index] == 0:
                self.swap(arr,index,length)
                index += 1
            index += 1
                
                
    #swap all elements
    def swap(self,arr,index,length):
        while index < length:
            arr[length] = arr[length -1]
            length -= 1
        
                
                
            
        
#         left = 0
#         length = len(arr)
#         print(length)
#         while left  <  length:
#             if arr[left] == 0:
#                 arr.insert(left,0)
#                 left += 2
#             else:
#                 left += 1
        
#         while len(arr) > length:
#             arr.pop()
#         # arr = arr[:length]
#         print(arr)
#         print(arr[:length])
        '''
         8
         1,0, 0,2,3,0,0,4,5,0,0
         
        '''
        
       #  [1,0,2,3,0,4,5,0]
       #     i
       # [1,0,2,3,0,4,5,0]
       #   i
       #  while j > i
       #      arr[j]= arr[j-1]
       #      j -=1
        