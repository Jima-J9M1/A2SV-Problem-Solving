# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        ptr1 = head
        start = head
        count = 1
        
        if not head:
            return
        while tail.next:
            tail = tail.next
            count += 1
            
        k = k % count
        idx = count - k
        
        for _ in range(idx-1):
            ptr1 = ptr1.next
            # print(ptr1.val)''
        if not ptr1.next:
            return head
        
        new_head = ptr1.next
        ptr1.next = None
        tail.next = head
        
        
        return new_head
        
            
            
        