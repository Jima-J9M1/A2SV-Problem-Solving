class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top,bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            #get col value from left to the right
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1

            #get row value from right to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            #get col value reverse way
            for i in range(right - 1,left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            #get row value reverse way
            for i in range(bottom - 1,top - 1,-1):
                res.append(matrix[i][left])
            left += 1
            
        return res
            
        
        