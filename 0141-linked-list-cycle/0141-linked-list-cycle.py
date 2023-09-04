# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast or (fast and fast.next == slow):
                return True
            
        
        return False
            
        
        
        
        
        
        
        
        
        
        
        
#         dic = {}
#         if not head:
#             return False
        
#         while head.next and head.next not in dic:
#             dic[head] = 1
#             head = head.next
            
#         if head.next in dic:
#             return True
        
#         return False
