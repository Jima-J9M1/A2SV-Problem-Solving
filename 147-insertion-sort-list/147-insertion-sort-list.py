# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = Dummy = ListNode(0)
        Dummy.next = head
        cur = head.next
        
        count = 1
        
        while cur:
            
            ptr2 = ptr1.next
            for i in range(count):
                if ptr2.val > cur.val:
                    temp = cur.val
                    cur.val = ptr2.val
                    ptr2.val = temp
                    
                ptr2 = ptr2.next
            
            
            count += 1
            cur = cur.next
            
        return Dummy.next
            
        