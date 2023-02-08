# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head
        
        if head == None  or head and head.next == None:
            return None
        
        
        left = left.next
        right = right.next.next
        
        while right and right.next and left != right :
            left = left.next
            right = right.next.next
        
        if right is None or right.next is None:
            return None
        
        
        left = head
        count = 0
        
        while right and left != right:
            count += 1
            left = left.next
            right = right.next
            
        return right