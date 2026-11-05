# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        res = []
        stack = []
        cur =  head
        index  = 0
        while cur:
            res.append(0)
            while stack and stack[-1][1] < cur.val:
                idx , _ = stack.pop()
                res[idx] = cur.val 
            stack.append((index , cur.val)) 
            index += 1
            cur = cur.next
        return res

            