class MyStack:

    def __init__(self):
        self.front=-1
        self.rear=-1
        self.queue=[]
        

    def push(self, x: int) -> None:
        if self.rear==-1 and self.front==-1:
            self.rear=0
            self.front=0   
        else:
            self.rear+=1
        self.queue.insert(self.rear,x)

    def pop(self) -> int:
        if self.empty()==False:
            y=self.queue[self.rear]
            self.queue.remove(self.queue[self.rear])
            self.rear-=1
            return y
        
        
        

    def top(self) -> int:
        if self.empty()==False:
            return self.queue[self.rear]
        return -1
        

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
