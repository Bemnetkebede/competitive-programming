# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        my_set = {head.val}
        curr = head
        while  curr.next:
            if curr.next.val in my_set:
                curr.next = curr.next.next
            else:
                my_set.add(curr.next.val)
                curr = curr.next
        return head


    