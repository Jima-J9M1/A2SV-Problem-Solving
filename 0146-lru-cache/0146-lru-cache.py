class Node:
    
    def __init__(self,key,value,next=None, prev = None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1 
        
        node = self.dic[key]
        value = node.val
        self.deleteNode(node)
        self.addToHead(node)
        
        return value

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            
            node = self.dic[key]
            self.deleteNode(node)
            self.addToHead(node)
            node.val = value
            
            
        else:
            
            if len(self.dic) == self.capacity:
                node = self.tail.prev
                self.deleteNode(node)
                del self.dic[node.key]
            
            newNode = Node(key,value)
            self.addToHead(newNode)
            self.dic[newNode.key] = newNode

        
    def addToHead(self,node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)