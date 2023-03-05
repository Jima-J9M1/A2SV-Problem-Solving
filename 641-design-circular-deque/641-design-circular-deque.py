class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [None]*(k+1)
        self.length = (k+1)
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull() == False:
            if self.queue[self.front] != None:
                self.front -= 1 if self.front != 0 else - (self.length-1)
                self.queue[self.front] = value
                
            else:
                self.queue[self.front] = value
                self.rear += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.isFull() == False:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1)%self.length
            return True
        return False
                

    def deleteFront(self) -> bool:
        if self.isEmpty() == False:
            self.queue[self.front] = None
            self.front = (self.front +1)%self.length
            return True
        return False

    def deleteLast(self) -> bool:
        if self.isEmpty() == False:
            self.rear -= 1 if self.rear != 0 else - (self.length-1)
            self.queue[self.rear] = None 
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty() == False:
            return self.queue[self.front]
        return -1

    def getRear(self) -> int:
        if self.isEmpty() == False:
            return self.queue[self.rear- 1 if self.rear != 0 else + (self.length-1)]
        return -1

    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True 
        return False

    def isFull(self) -> bool:
        if self.front > self.rear and self.front-self.rear == 1:
            return True
        elif self.rear > self.front and self.rear - self.front == self.length -1:
            return True 
        return False