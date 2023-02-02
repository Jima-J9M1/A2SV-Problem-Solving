# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = head
        
        while left:
            right = left
            
            while right and right.val >= x:
                right = right.next
            
            if not right:
                return head
            
            if right != left:
                temp = right.val
                ptr = left
                
                while ptr != right:
                    temp, ptr.val = ptr.val, temp
                    ptr = ptr.next
                
                ptr.val = temp

            
            left = left.next
            
            
        return head
            
            
            
            
            
            
            
            
        