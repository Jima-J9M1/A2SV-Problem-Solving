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
                
                min_val = heap[0]
                
                if ele - min_val[0] == 1:
                    heappop(heap)
                    heapq.heappush(heap, [ele, min_val[1] + 1])
                    
                elif ele - min_val[0] > 1:
                    
                    while heap and ele - heap[0][0] > 1:
                        if min_val[1] < 3:
                            return False
                        
                        min_val = heappop(heap)
                    
                    if heap:
                        min_val = heap[0]
                        if ele - min_val[0] == 1:
                            heappop(heap)
                            heapq.heappush(heap, [ele, min_val[1] + 1])
                            
                        else:
                            heapq.heappush(heap,[ele, 1])
                            
                    else:
                        heapq.heappush(heap, [ele, 1])
                        
                else:
                    heapq.heappush(heap, [ele, 1])
                    
        for val, l in heap:
            if l < 3:
                ans = False
                
        return ans