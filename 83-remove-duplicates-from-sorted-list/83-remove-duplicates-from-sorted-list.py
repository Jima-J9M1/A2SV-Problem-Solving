# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        left = head
        
        while cur:
            
            if cur.val != left.val:
                
                if left != cur:
                    left.next = cur
                    left = left.next
            
            cur = cur.next
            
        if left and left.next:
            left.next = None
            
            
        return head
                    