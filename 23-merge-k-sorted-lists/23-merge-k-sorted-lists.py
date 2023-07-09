# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedList = []
        
        for index in range(len(lists)):
            head = lists[index]
            while head:
                heappush(sortedList, head.val)
                head = head.next
        
        mergeLinkedList = ListNode(0)
        head = mergeLinkedList
        
        while sortedList:
            val = heappop(sortedList)
            newNode = ListNode(val)
            head.next = newNode
            head = head.next
            
        return mergeLinkedList.next