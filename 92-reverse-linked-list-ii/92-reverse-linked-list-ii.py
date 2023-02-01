# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        Dummy  = ListNode(0,head)
        cur = head
        ptr1 = Dummy
        
        for i in range(left - 1):
            ptr1 = cur
            cur = cur.next
        
        prev = None
        
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        ptr1.next.next = cur
        ptr1.next = prev
        
        return Dummy.next
        
        
        
        
        
        
        # while cur:
        #     print(cur)
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
            
        # print(prev)
            