# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        res = []
        ptr = head
        
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        left = 0
        right = len(res) - 1
        ans = []
        while left < right:
            ans.append(res[left])
            ans.append(res[right])
            
            left += 1
            right -= 1
        
        if len(res) % 2 == 1:
            ans.append(res[left])
            
            
        for i in range(len(ans)):
            ptr.val = ans[i]
            ptr = ptr.next
        
        
        