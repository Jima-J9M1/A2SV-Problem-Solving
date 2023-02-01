class Node:
    
    def __init__(self,val = None):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        count = 0
        cur = self.head
        
        while cur and count != index:
            cur = cur.next
            count += 1
            
        if cur == None:
            return -1
        
        return cur.val
        
            

    def addAtHead(self, val: int) -> None:

        new_node = Node(val)
            
        new_node.next = self.head
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        
        new_node = Node(val)
        cur = self.head
        
        if self.head == None:
            self.head = new_node
            return
        
        while cur.next != None:
            cur = cur.next

        
        cur.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        
        new_node = Node(val)
        cur = self.head
        
        if index == 0:
            if self.head != None:
                new_node.next = self.head
                self.head = new_node
                
            else:
                self.head = new_node
        
        count = 0
        
        while cur and count !=  index - 1:
            cur = cur.next 
            count += 1
        
        if cur == None:
            return
        
        new_node.next = cur.next
        cur.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        count = 0

        if index == 0:
            self.head = self.head.next
            return
        
        while cur.next and count != index - 1:
            cur = cur.next
            count += 1
        
        if cur.next == None:
            return
        
        cur.next = cur.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)