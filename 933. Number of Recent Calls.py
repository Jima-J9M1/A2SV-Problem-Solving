class RecentCounter:

    def __init__(self):
        self.queue=[]
        self.count=[]
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count.append(len(self.queue))
        while self.queue[-1]-self.queue[0]>3000:
            self.count.remove(len(self.queue))
            self.queue.pop(0)
        return len(self.count)
