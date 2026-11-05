class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:
    def __init__(self):
        self.node = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.node
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endofword = True
    
    def search(self, word: str) -> bool:
        node = self.node
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.endofword    

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
