import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        final=[]
        for i in points:
            res=[]
            res.append(pow(i[0],2)+pow(i[1],2))
            res.append(i)
            final.append(res)
        final.sort()
        i=0
        result=[]
        while i<k:
            result.append(final[i][1])
            i+=1


        return result


        
