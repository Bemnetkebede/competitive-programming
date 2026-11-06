# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = l1
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        pr = None
        t = l2
        while t:
            temp = t.next
            t.next = pr
            pr = t
            t = temp
        
        nums1 = 0
        cu = prev
        while cu:
            nums1 = nums1 * 10 + cu.val
            cu = cu.next
        
        nums2 = 0
        cu = pr
        while cu:
            nums2 = nums2 * 10 + cu.val
            cu = cu.next
        
        total = nums1 + nums2
        total = ((str(total)[::-1]))
        dummy = ListNode()
        cur = dummy
        i = 0
        while i < len(total):
            cur.next = ListNode(int(total[i]))
            cur = cur.next
            i += 1
        return dummy.next

        

        