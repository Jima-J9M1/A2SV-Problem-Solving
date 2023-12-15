class Node:
    def __init__(self,val,key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.dic_ = dict()
        
        

    def get(self, key: int) -> int:
        if key not in self.dic_:
            return -1
        
        node = self.dic_[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.dic_:
            node = self.dic_[key]
            node.val = value
            
            self.removeNode(node)
            self.addNode(node)
            
            
        else:
            if len(self.dic_) == self.capacity:
                del_node =  self.tail.prev 
                self.removeNode(del_node)
                del self.dic_[del_node.key]
            

            new_node = Node(value, key)
            self.addNode(new_node)
            self.dic_[key] = new_node
        
            
        
            
        
    
    def addNode(self, new_node):
            cur_head = self.head.next
            self.head.next = new_node
            new_node.next = cur_head
            cur_head.prev = new_node
            new_node.prev = self.head
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)