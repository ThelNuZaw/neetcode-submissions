class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, words):
        cur = self
        for w in words:
            if w not in cur.children:
                cur.children[w] = TreeNode()
            cur = cur.children[w]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TreeNode()
        
        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        visit = set()
        res = set()
        def dfs(r, c, word, node):
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)

            dfs(r + 1, c, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r, c - 1, word, node)

            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", root)
        return list(res)