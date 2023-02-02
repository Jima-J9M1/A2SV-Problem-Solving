# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        size = 0
        left = head
        
        while cur:
            cur = cur.next
            size += 1
        
        
        
        if n > size or size == 1:
            return
        
        idx = size - n
        
        if idx == 0:
            return head.next
        
        for _ in range(idx - 1):
            left = left.next
        
        if left and left.next:
            left.next = left.next.next
        
    
        return head
            
        