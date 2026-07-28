class Solution:
    def countSubstrings(self, s: str) -> int:
        resLen = 0
        res = ""
        count = 0
        #think like start at the middle and expand left and right
        #odd length
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                if (r - l + 1) > resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        #even length
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                if (r - l + 1) > resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return count