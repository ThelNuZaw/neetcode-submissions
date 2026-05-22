class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.Endwith = False

    def insert(self, word: str) -> None:
        
        curr = self
        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                newnode = PrefixTree()
                curr.children[index] = newnode
            curr = curr.children[index]
        curr.Endwith = True
            
 
    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.Endwith
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for p in prefix:
            index = ord(p) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
            
        