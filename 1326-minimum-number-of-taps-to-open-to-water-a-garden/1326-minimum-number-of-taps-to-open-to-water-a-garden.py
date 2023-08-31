class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        for indx, val in enumerate(ranges):
            range_1 = indx - val 
            range_2 = indx + val
            ranges[indx] = [range_1, range_2]
            
        ranges.sort()
        flag = False
        minEle = ranges[0]
        min_range = 0
        max_range = minEle[1]
        min_tabs = 0
        
        for indx in range(1, len(ranges)):
            r_1, r_2 = ranges[indx]
            
            if r_1 <= min_range:
                if r_2 > max_range:
                    minEle = ranges[indx]
                    max_range = minEle[1]
                    if minEle[1] >= n:
                        flag = True
                        min_tabs += 1
                        break
                        
            else:
                min_tabs += 1
                if (max_range - ranges[indx][0]) < 0:
                    print("what")
                    flag = False
                    break
                    
                min_range = max_range
                minEle = ranges[indx]
                max_range = minEle[1]
        
        
        return min_tabs if flag else -1     
