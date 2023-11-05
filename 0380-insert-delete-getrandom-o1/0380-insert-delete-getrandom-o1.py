class RandomizedSet:

    def __init__(self):
        self.item = {}
        self.data = []
        

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        
        self.item[val] = len(self.data)
        
        self.data.append(val)
        
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        
        last_element = self.data[-1]
        last_indx_element = self.item[val]
        
        self.data[last_indx_element] = last_element
        self.item[last_element] = last_indx_element
        
        self.data[-1] = val
        self.data.pop()
        self.item.pop(val)
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()