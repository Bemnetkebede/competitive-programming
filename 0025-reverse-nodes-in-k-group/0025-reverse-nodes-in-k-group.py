# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        prev_group = dummy
        
        while head:
            temp = head
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1
            if count < k:
                return dummy.next 
            prev, cur = None, head
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            prev_group.next = prev
            head.next = cur
            prev_group = head
            head = cur
        return dummy.next
        
    