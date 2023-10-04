# class Node:
#     def __init__(self,val):
#         self.next = None
#         self.val = val

class MyHashMap:
    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        if len(self.hashmap) <= key:
            self.hashmap += [-1] * (key - len(self.hashmap)+1)
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key] if key < len(self.hashmap) else -1

    def remove(self, key: int) -> None:
        if key < len(self.hashmap):
            self.hashmap[key] = -1

#     def __init__(self):
#         self.head = Node([-1, -1])
        

#     def put(self, key: int, value: int) -> None:
#         cur = self.head
#         new_node = Node([key, value])
        
#         if not cur:
#             cur = new_node
#         else:
            
#             while cur.next and cur.val[0] != key:
#                 cur = cur.next
                
#             if cur.val[0] == key:
#                 cur.val[1] = value
#             else:
#                 cur.next = new_node
        

#     def get(self, key: int) -> int:
#         cur = self.head
        
#         while cur:
#             if cur.val[0] == key:
#                 return cur.val[1]
            
#             cur = cur.next

#         return -1
    
#     def remove(self, key: int) -> None:
#         cur = self.head
        
#         if not cur.next:
#             return
            
#         prev = None
        
        
#         while cur and cur.val[0] != key:
#             prev = cur
#             cur = cur.next
        
#         if cur:
#             prev.next = cur.next
        
    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)