class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        
        if len(s) < 2 or numRows == 1:
            return s
            
        col1 = len(s) // numRows
        rem = len(s) % numRows
        length = ( col1 * numRows) + ( col1 - 1 ) * (numRows - 2) 

        if length > len(s) or rem == 0:
            col2 = ( col1 - 1 ) * (numRows - 2)
        else:
            col2 = rem
        col = col1 + col2
        
        grid = []

        for _ in range(numRows):
            row_val = ["0"] * col
            grid.append(row_val)

        right = 0
        row,col = 0,0


        while right < len(s):


            while right < len(s) and row < numRows - 1:
                grid[row][col] = s[right]
                row += 1
                right += 1


            if right >= len(s):
                break

            grid[row][col] = s[right]
            right += 1

            count = 0
            
            
            while right < len(s) and count < numRows - 2:
                row -= 1
                col += 1
                
                grid[row][col]
                grid[row][col] = s[right]
                right += 1
                count += 1


            if right >= len(s):
                break

            row -= 1
            col += 1



        res = []

        for row in range(len(grid)):

            for col in range(len(grid[0])):

                if grid[row][col] != '0':
                    res.append(grid[row][col])

        return "".join(res)