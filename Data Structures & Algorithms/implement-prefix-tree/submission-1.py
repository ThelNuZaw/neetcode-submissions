class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TreeNode()
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isEnd 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            index = ord(p) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
        