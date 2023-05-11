class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        nums.sort()
        count = Counter(nums)
        heap = []
        ans = True
        
        for ele in nums:
            if not heap:
                heapq.heappush(heap,[ele,1])
                
            else:
                
                while heap and ele - heap[0][0] > 1:
                        if heap[0][1] < 3:
                            return False
                        
                        heappop(heap)
                
                if not heap or ele - heap[0][0] != 1:
                    heappush(heap, [ele,1])
                    
                else:
                    heappush(heap, [ele, heappop(heap)[1] + 1])

                    
        for val, l in heap:
            if l < 3:
                ans = False
                
        return ans