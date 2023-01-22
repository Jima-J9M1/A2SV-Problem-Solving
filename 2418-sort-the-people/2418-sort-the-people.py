class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        max_val = max(heights)
        arr = [0] * (max_val + 1)
        
        for index in range(len(heights)):
            arr[heights[index]] = names[index]
            
        res = []
        for index in range(len(arr) - 1, -1,-1):
            if arr[index]:
                res.append(arr[index])
                
        
           
        return res