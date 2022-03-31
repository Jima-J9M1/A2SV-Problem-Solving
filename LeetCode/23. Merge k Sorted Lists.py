# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res= []
        
        for link in lists:
            newNode = link
            while newNode:
                res.append(newNode.val)
                newNode = newNode.next
        res.sort()
        
        Node_result = ListNode()
        tail = Node_result
        i = 0
        while i < len(res):
            tail.next = ListNode(res[i])
            tail = tail.next
            i+=1
        return Node_result.next
 
#         newNode = ListNode()
#         tail = newNode
#         i = 0
#         N = 0
        
#         while i < len(lists):
#             while lists[i]:
#                 tail.next = lists[i]
#                 lists[i] = lists[i].next
#                 tail = tail.next
#                 N+=1
#             i +=1
#         i=0
#         while i < N:
#             j = 0
#             cur = newNode.next
#             while j< N -i and cur.next:
#                 if cur.val > cur.next.val:
#                     cur.val, cur.next.val = cur.next.val,cur.val
#                 cur = cur.next
#                 j+=1
#             i+=1
#         return newNode.next
