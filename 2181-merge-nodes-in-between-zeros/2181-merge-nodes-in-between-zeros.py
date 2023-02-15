# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Dummy = ListNode(0)
        ptr2 = Dummy
        cur = head.next
        res = 0
        
        while cur:
            
            if cur.val == 0:
                new_node = ListNode(res,None)
                ptr2.next = new_node
                ptr2 = ptr2.next
                res = 0
            
            res += cur.val
            cur = cur.next
        
        return Dummy.next
                
                
                
        