class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Node:
    def __init__(self, dic):
        self.root = TreeNode()
        
        for w in dic:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TreeNode()
                cur = cur.children[c]
            cur.isEnd = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s): 0} #min extra character from index i to the end of string
        trie = Node(dictionary).root

        def dfs(i):
            curr = trie
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1) #skip the character
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isEnd:
                    res = min(res,dfs(j + 1))
            dp[i] = res
            return res 
        return dfs(0)