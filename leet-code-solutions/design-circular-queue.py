class MyCircularQueue:

    def __init__(self, k: int):
        self.f = -1
        self.r = -1
        self.queue = []
        self.k = k
        self.size = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if len(self.queue) < self.k:
            if self.f == -1:
                self.f += 1
                
            self.queue.append(value)
            self.r += 1
            self.size += 1
            return True
        
        if self.r == self.k - 1:
            self.r = -1
        
        self.r += 1
        self.queue[self.r] = value
        self.size += 1
        
        
        return True

    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.f == self.k - 1:
            self.f = -1
            
        self.f += 1
        self.size -= 1
        
        
        return True
        
        
            
            

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.r]
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        
        
        return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()