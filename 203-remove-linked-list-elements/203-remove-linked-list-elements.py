# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        Dummy = ListNode(0,head)
        prev = Dummy
        cur = head
        
        while cur:
            
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
                continue
            
            prev = cur
            cur = cur.next
        
        return Dummy.next