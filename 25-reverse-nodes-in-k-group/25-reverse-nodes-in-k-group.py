# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        Dummy = ListNode(0,None)
        ptr = Dummy
        cur = head
        left = head
        count = 0
        
        while cur:
            
            if count == k:
                
                
                prev = None
                for i in range(count):
                    temp = left.next
                    left.next = prev
                    prev = left
                    left = temp
                    
                count = 0
                ptr.next = prev
                
                while ptr.next:
                    ptr = ptr.next
                
                
            count += 1
            cur = cur.next
            
        if count == k:
            
            prev = None
            
            for i in range(count):
                temp = left.next
                left.next = prev
                prev = left
                left = temp
            
            ptr.next = prev
        else:
            ptr.next = left
            
        
        return Dummy.next   
        
        
            
            
            
            
        