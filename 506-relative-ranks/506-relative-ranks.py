class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for i in range(len(score)):
            heap.append([-score[i], i])
            
        heapq.heapify(heap)
        i = 1
        res = [0]* len(score)
        while heap:
            val = heapq.heappop(heap)
            if i == 1:
                res[val[1]] = "Gold Medal"
            elif i == 2:
                res[val[1]] = "Silver Medal"

            elif i == 3:
                res[val[1]] = "Bronze Medal"

            else:
                res[val[1]] = str(i)
                
            i += 1
                
        return res
            
            