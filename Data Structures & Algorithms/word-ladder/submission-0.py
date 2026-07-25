class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        wordList.append(beginWord)
        patternmap = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                patternmap[pattern].append(word) # *it : [hit,..]
        
        q = deque([beginWord])
        res = 1
        visit = set((beginWord))
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    w_pattern = word[:j] + "*" + word[j+1:]
                    for nei in patternmap[w_pattern]:
                        if not nei in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1
        return 0
                