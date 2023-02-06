# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenNode ,oddNode = ListNode(0), ListNode(0)
        even = evenNode
        odd = oddNode
        
        cur = head
        size = 0
        
        if not head:
            return
        
        
        while cur:
            cur = cur.next
            size += 1
        
        cur = head
        next_ = cur.next
        count = 1
        
        while next_ and count < size + 1:
            if count % 2 == 0:
                cur.next = None
                even.next = cur
                even = even.next
            else:
                cur.next = None
                odd.next = cur
                odd = odd.next
                
        
            cur = next_
            next_ = next_.next
            count += 1
        
        if size % 2 == 0:
            even.next = cur
            even = even.next
        else:
            odd.next = cur
            odd = odd.next
            
        even.next = None
        odd.next = evenNode.next
        
        return oddNode.next
        
        
        
            
            