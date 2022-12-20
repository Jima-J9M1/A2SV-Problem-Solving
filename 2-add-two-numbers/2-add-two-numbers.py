# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode()
        res = sum
        s = 0
        k = 0
        while l1 or l2:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            valu = v2 + v1 + s
            k = valu % 10
            s = valu // 10
            sum.next = ListNode(k)
            sum = sum.next
        if s:
            sum.next = ListNode(s)
        

        return res.next