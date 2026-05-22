class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        length = 0
        l = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            length = max(length, r - l + 1)
        return length