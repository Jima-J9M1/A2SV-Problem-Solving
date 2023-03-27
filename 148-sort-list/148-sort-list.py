# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left_node, right_node):
            ptr1 = right_node
            ptr2 = left_node
            Dummy = ListNode(0)
            next = Dummy
            
            while ptr1 != None and ptr2 != None:
                
                if ptr1.val < ptr2.val:
                    new_node = ListNode(ptr1.val)
                    next.next = new_node
                    next = new_node
                    ptr1 = ptr1.next
                else:
                    new_node = ListNode(ptr2.val)
                    next.next = new_node
                    next = new_node
                    ptr2 = ptr2.next
                    

            if ptr1:
                next.next = ptr1
            
            if ptr2:
                next.next = ptr2

            return Dummy.next
        
        
        def middle(head):
            left_dummy = ListNode(0)
            frist_node = head
            slow = head
            fast = head.next 
            left = slow
            cur = head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None

            return [frist_node, right]
        
        def mergeSort(node):
            
            if not node or  node.next is None:
                return node
            
            node = middle(node)
            left_node = node[0]
            right_node = node[1]
            

            left = mergeSort(left_node)
            right = mergeSort(right_node)
            
            return merge(left, right)
        
        # ans = mergeSort(head)
        return mergeSort(head)
        # print(ans)
            
            
            
            
            
            
                    
                    
                
            