class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.k = k
        self.dic = defaultdict(int)
        self.val = value
        
    def consec(self, num: int) -> bool:
        self.dic[num] += 1
        self.queue.append(num)
        
        if len(self.queue) == self.k:
            if num == self.val and self.dic[num] == self.k:
                return True
            
        elif len(self.queue) > self.k:
            
            new_val = self.queue.popleft()
            self.dic[new_val] -= 1
            if self.dic[new_val] == 0:
                del self.dic[new_val]
            
            if num == self.val and self.dic[num] == self.k:
                return True
         
        return False 
                
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)