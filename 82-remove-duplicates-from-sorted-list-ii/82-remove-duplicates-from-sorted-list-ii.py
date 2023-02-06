# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Dummy = ListNode(0)
        pointer = Dummy
        Dummy.next = head
        
        while head and head.next:
            if head.next.val == head.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next


                head = head.next
                pointer.next = head
            else:
                pointer = pointer.next
                head = head.next
        
        return Dummy.next
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         node = pointer =ListNode(0)
#         node.next = head

        
#         while head and head.next:
#             if head.val == head.next.val:
#                 while head and head.next and head.val == head.next.val:
#                     head = head.next
#                 head = head.next
#                 pointer.next = head
#             else:
#                 pointer = pointer.next
#                 head = head.next
        
#         return node.next
        # [1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5]
        # [1 -> 2 -> 3 -> 4]