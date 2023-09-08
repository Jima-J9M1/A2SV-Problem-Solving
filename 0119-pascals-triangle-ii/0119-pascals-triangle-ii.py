class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result = [[1]]
        
        def rec(numRows):
            if numRows == 1:
                return
            
            if numRows == 2:
                result.append([1,1])
                return [1,1]
            
            ans = rec(numRows - 1)
            res = []
            
            for i in range(len(ans) - 1):
                res.append(ans[i] + ans[i + 1])
            
            ans = [1] + res + [1]
            result.append(ans)
                
                
            return ans
        
        rec(rowIndex + 1)
        return result[rowIndex]