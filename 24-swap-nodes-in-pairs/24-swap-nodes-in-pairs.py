# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        Dummy = ListNode(0)
        cur = Dummy
        left = head
        right = head.next
        
        while left and right:
            temp = right.next
            left.next = temp
            right.next = left
            cur.next = right
            
            if left and left.next: 
                right = left.next.next
                cur = cur.next.next
                left = left.next
                continue
            break
            
        return Dummy.next
                  
            