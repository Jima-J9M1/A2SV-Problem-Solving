class DataStream:

    def __init__(self, value: int, k: int):
        #Intaililze queue 
        self.queue = deque()
        self.k = k
        self.dic = defaultdict(int)
        self.val = value
        
    def consec(self, num: int) -> bool:
        self.dic[num] += 1
        self.queue.append(num)
        
        #compute if the value and lenght of the queue is equal to the given value and if true return True
        if len(self.queue) == self.k:
            if num == self.val and self.dic[num] == self.k:
                return True
        
        #Check if the value of the length of the queue is grreater than the given size 
        elif len(self.queue) > self.k:
            
            #remove the element from the begining and delete from the dictonary if the val is zero
            new_val = self.queue.popleft()
            self.dic[new_val] -= 1
            if self.dic[new_val] == 0:
                del self.dic[new_val]
            
            #After the pop operation and delete operation check if the remaining of the queue equa with value and length of the given
            if num == self.val and self.dic[num] == self.k:
                return True
         
        return False 
                
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)