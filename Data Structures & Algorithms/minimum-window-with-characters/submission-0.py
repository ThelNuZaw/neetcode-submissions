class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = {}
        window = {}
        for ct in t:
            countT[ct] = 1 + countT.get(ct, 0)

        have = 0
        need = len(countT)
        res = [-1,-1]
        resLength = float("infinity")
        l = 0
        for r in range(len(s)):
            key = s[r]
            window[key] = 1 + window.get(key, 0)

            if key in countT and window[key] == countT[key]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLength:
                    res = [l, r]
                    resLength = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLength != float("infinity") else ""