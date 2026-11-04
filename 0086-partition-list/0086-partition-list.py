# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy_small = ListNode()
        dummy_greater = ListNode()

        small_cur = dummy_small
        greater_cur = dummy_greater

        cur = head
        while cur:
            if cur.val < x:
                small_cur.next = cur
                small_cur = small_cur.next
            else:
                greater_cur.next = cur
                greater_cur = greater_cur.next
            cur = cur.next
        greater_cur.next = None
        small_cur.next = dummy_greater.next
        return dummy_small.next
