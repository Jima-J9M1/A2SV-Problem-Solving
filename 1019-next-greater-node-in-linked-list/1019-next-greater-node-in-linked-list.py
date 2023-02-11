# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        next_greater = []
        cur = head
        
        while cur:
            next_greater.append(cur.val)
            cur = cur.next
            
        
        stack = []
        right = 0
        res = [0] *len(next_greater)
        
        while right < len(next_greater):
            
            if stack and next_greater[stack[-1]] < next_greater[right]:
                print(stack)
                while stack and next_greater[right] > next_greater[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = next_greater[right]
            
            stack.append(right)
            right += 1
            
        ptr = head
        
        return res
        
            
        