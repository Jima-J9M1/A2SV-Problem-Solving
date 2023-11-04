class OrderedStream:

    def __init__(self, n: int):
        self.pos = 1
        self.stream = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ans = []
        while self.pos in self.stream:
            ans.append(self.stream[self.pos])
            self.pos += 1
            
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)