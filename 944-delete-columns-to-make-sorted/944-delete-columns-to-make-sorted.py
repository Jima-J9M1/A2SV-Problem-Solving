class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        
        for col in range(len(strs[0])):
            col_val = []
            
            for row in range(len(strs)):
                if col_val and col_val[-1] > strs[row][col]:
                    count += 1
                    break
                col_val.append(strs[row][col])
                
#                 col_val.append(strs[row][col])
            
#             sorted_col = sorted(col_val)
            
#             if sorted_col != col_val:
#                 count += 1
        
        return count
        