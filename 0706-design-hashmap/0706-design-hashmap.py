class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

class MyHashMap:

    def __init__(self):
        self.head = Node([-1, -1])
        

    def put(self, key: int, value: int) -> None:
        cur = self.head
        new_node = Node([key, value])
        
        if not cur:
            cur = new_node
        else:
            
            while cur.next and cur.val[0] != key:
                cur = cur.next
                
            if cur.val[0] == key:
                cur.val[1] = value
            else:
                cur.next = new_node
        

    def get(self, key: int) -> int:
        cur = self.head
        
        while cur:
            if cur.val[0] == key:
                return cur.val[1]
            
            cur = cur.next

        return -1
    
    def remove(self, key: int) -> None:
        cur = self.head
        
        if not cur.next:
            return
            
        prev = None
        
        
        while cur and cur.val[0] != key:
            prev = cur
            cur = cur.next
        
        if cur:
            prev.next = cur.next
        
    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)