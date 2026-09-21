class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        visit = set()
        maxl = 1
        while right < len(s):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1

            visit.add(s[right])
            maxl = max(maxl, right - left + 1)
            right += 1
        return maxl