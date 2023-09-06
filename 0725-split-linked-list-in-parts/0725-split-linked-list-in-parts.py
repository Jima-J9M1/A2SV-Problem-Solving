# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            
        result = []
        cur = head
        if count <= k:
            for i in range(k):
                new_node = copy.copy(cur)
                if new_node:
                    new_node.next = None
                    result.append(new_node)
                else:
                    result.append(None)
                    
                if cur:
                    cur = cur.next
                
        else:
            cur = head
            parts = count // k
            rem = count % k
            for i in range(k):
                
                right = 0
                new_node = ListNode()
                new_node.next = cur
                ptr = new_node
                while right < parts:
                    if ptr:
                        ptr = ptr.next
                    if cur:
                        cur = cur.next
                    
                    right += 1
                    
                if rem:
                    ptr = ptr.next
                    rem -= 1
                    cur = cur.next
                    
                
                if ptr:
                    ptr.next = None
                    
                result.append(new_node.next)
                    
                
                    
        return result
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    