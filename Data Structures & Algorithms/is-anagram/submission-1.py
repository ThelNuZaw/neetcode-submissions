class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        shash = {}
        thash = {}

        for i in range(len(s)):
            shash[s[i]] = shash.get(s[i], 0) + 1
            thash[t[i]] = thash.get(t[i], 0) + 1
        return True if shash == thash else False
        