# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res= []
        
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        stack = []
        
        for i in range(len(res)):
            
            while stack and stack[-1] < res[i]:
                stack.pop()
            
            stack.append(res[i])
            
        Node = ListNode(0)
        ptr = Node
        
        
        for i in range(len(stack)):
            new_node =  ListNode(stack[i])
            ptr.next = new_node
            ptr = ptr.next
        
        return Node.next