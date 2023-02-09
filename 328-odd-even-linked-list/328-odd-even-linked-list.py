# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = evenNode = ListNode(0)
        odd = oddNode = ListNode(0)
        count = 1
        while head:
            
            if count % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            
            head = head.next
            count += 1
        
        even.next = None
        
        odd.next = evenNode.next
        
        return oddNode.next