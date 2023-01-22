class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        max_val = max(heights)
        arr = [0] * (max_val + 1)
        arr_names = [0] * (max_val + 1)
        
        for index in range(len(heights)):
            arr[heights[index]] = 1
            arr_names[heights[index]] = names[index]
            
        res = []
        for index in range(len(arr) - 1, -1,-1):
            if arr[index] > 0:
                res.append(arr_names[index])
                
        
           
        return res