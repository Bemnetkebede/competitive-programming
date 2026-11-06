class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self, val=0):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        return cur.val 

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.next = None
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: 
            return
        if index < 0:  
            index = 0 
        cnt = 0
        cur = self.dummy
        while cur and cnt < index:
              cur = cur.next
              cnt += 1
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: 
            return
        cnt = 0
        cur = self.dummy
        while cur and cnt < index:
           cur = cur.next
           cnt += 1
        cur.next = cur.next.next 
        self.size -= 1
