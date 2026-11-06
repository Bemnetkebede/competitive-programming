# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Find the middle of the linked list
        middle = self.find_middle(head)
        second_half = middle.next
        middle.next = None
        
        # Step 2: Recursively sort the first and second halves
        sorted_first_half = self.sortList(head)
        sorted_second_half = self.sortList(second_half)
        
        # Step 3: Merge the sorted halves
        return self.merge(sorted_first_half, sorted_second_half)
    
    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next