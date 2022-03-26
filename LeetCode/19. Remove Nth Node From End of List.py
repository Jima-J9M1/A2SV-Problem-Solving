# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newNode = ListNode()
        tail = newNode
        secNode = ListNode()
        rear = secNode
        i = 0
        j = 1
        while head:
            rear.next = head
            head = head.next
            rear = rear.next
            i +=1
        secNode = secNode.next
        while j <= ( i - (n-1)) and secNode:
            if j == ( i - (n-1)) :
                tail.next = secNode.next
            else:
                tail.next = secNode
            secNode = secNode.next
            tail = tail.next

            j +=1
            
        return newNode.next
            
