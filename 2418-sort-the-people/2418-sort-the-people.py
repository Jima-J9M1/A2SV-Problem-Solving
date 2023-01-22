class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for index in range(1,len(heights)):
            right = index
            height_val = heights[right]
            names_val = names[right]
            
            #sort each element to the left              
            while right > 0 and heights[right - 1] < height_val:
                heights[right] = heights[right - 1]
                names[right] = names[right - 1]
                right -= 1
                
            heights[right] = height_val            
            names[right] = names_val
           
        return names