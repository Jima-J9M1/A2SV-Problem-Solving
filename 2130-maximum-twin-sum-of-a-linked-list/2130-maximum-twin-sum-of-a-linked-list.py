# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        size = 0
        
        
        if not head.next.next:
            return head.val + head.next.val
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            size += 1
        
        prev = None
        ptr = slow
        
        
        while ptr:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        
        ptr = prev
        ptr2 = head
        max_val = 0
        
        for _ in range(size):
            cal = ptr.val + ptr2.val
            ptr = ptr.next
            ptr2 = ptr2.next
            max_val = max(max_val, cal)
            
        
        return max_val
            
        