# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dic_linked = dict()
        slow = head
        while slow.next and slow not in dic_linked:
            dic_linked[slow] = 1
            slow = slow.next
        
        
        if slow and slow.next == None:
            return None
        
        return slow
                
            