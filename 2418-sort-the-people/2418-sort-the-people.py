class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for index in range(len(names)):
            
            for j in range(len(names) - 1):
                
                if heights[j + 1] > heights[j]:
                    heights[j + 1], heights[j] = heights[j], heights[j + 1]
                    names[j + 1], names[j] = names[j], names[j + 1]
                    
        return names