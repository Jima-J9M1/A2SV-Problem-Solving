class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex - 1)# 4
        res  = [1] +  [prev[i] + prev[i + 1] for i in range(rowIndex - 1 )] + [1]
        
        return res
    
    
        