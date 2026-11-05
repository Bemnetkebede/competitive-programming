# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None          
            current = head       

            while current:
                next_node = current.next  
                current.next = prev       
                prev = current            
                current = next_node       

            return prev 
        head = reverse(head)
        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy
        current = head
        max_val = head.val
    
        while current:
            if current.val < max_val:
                prev.next = current.next
            else:
                max_val = current.val
                prev = current
            current = current.next
        return reverse(dummy.next) 


    