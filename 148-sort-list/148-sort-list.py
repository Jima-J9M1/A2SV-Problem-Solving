# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        res.sort()
        
        cur = head
        
        for i in range(len(res)):
            cur.val = res[i]
            cur = cur.next
        
        return head