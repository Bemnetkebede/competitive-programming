class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None 
        self.next = None  

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
    def remove_node(self, node):  
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:  
            target_node = self.cache[key]
            
           
            self.remove_node(target_node)
            self.add_to_tail(target_node)
            
            return target_node.val  
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        
      
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add_to_tail(new_node)
        
     
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self.remove_node(lru_node)
            del self.cache[lru_node.key] 