# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        No_over=[]
        intervals.sort()
        for i in intervals:
            if No_over==[] or No_over[-1][1] < i[0]:
                No_over.append(i)
            else:
                No_over[-1][1] = max(No_over[-1][1],i[1])
            
        return No_over
        
