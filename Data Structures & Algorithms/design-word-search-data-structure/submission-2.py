class TreeNode:
    def __init__(self):
        self.children = {} #{a:NodeA}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
          
            if w not in cur.children:
                cur.children[w] = TreeNode()
            cur = cur.children[w]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            cur = root
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEnd
        return dfs(0, self.root)