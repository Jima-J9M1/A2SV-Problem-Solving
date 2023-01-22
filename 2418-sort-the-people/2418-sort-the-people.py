class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for index in range(len(names) - 1, -1, -1):
            min_val = index
            
            for j in range(index):
                if heights[min_val] > heights[j]:
                    min_val = j
                    
            heights[min_val], heights[index] = heights[index], heights[min_val]
            names[min_val],names[index] = names[index], names[min_val]
                    
        return names