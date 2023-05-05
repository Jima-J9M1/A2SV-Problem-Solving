class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
       
            
        heap = []
        for key in count:
            heap.append((-count[key],key))

        heapq.heapify(heap)
        
        res = []
        temp = []
        freq = 0
        count = 0
        
        while heap and k > count  :
            word = heapq.heappop(heap)
            temp.append(word[1])
            count += 1
                
                
        
      
        
        return temp
            
            