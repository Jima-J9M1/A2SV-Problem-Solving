class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        col_grid = []
        length = len(grid)
        ans = []
        ans_row = []
        ans_col = []
        
        for index in range(len(grid[0])):
            res_col = [0,0]
            for j in range(length):
                if grid[j][index] == 1:
                    res_col[1] += 1
                else:
                    res_col[0] += 1
            
            ans_col.append(res_col)
            
        for index,ele in enumerate(grid):
            res = [0,0]
            for val in ele:
                if val == 1:
                    res[1] += 1
                else:
                    res[0] += 1
            ans_row.append(res)
        

        
        for ele in ans_row:
            res = []
            
            for val in ans_col:
                zero_res = ele[0] + val[0]
                one_res = ele[1] + val[1]
                cal = one_res - zero_res
                res.append(cal)
            ans.append(res)
            
        return ans
        
#             col_grid.append(res)
        
        
        
        
#         for index in range(len(grid[0])):
#             res = []
#             for j in range(length):
#                 res.append(grid[j][index])
                
#             col_grid.append(res)
        
#         for ele in grid:
#             res = []
            
#             for val in col_grid:
#                 count_zero = val.count(0) + ele.count(0)
#                 count_one = val.count(1) + ele.count(1)
#                 res.append(count_one - count_zero)
#             ans.append(res)
        

        
#         return ans
            
        