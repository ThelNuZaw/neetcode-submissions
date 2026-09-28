class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        countS = {}
        for ct in t:
            countT[ct] = 1 + countT.get(ct, 0)

        have = 0
        need = len(countT)
        res = [-1, -1]
        reslength = float('infinity')
        left = 0
        for right in range(len(s)):
            countS[s[right]] = 1 + countS.get(s[right], 0)

            if s[right] in countT and countS[s[right]] == countT[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < reslength:
                    res = [left, right]
                    reslength = right - left + 1
                countS[s[left]] -= 1
                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
            
        left, right = res
        return s[left: right + 1] if reslength != float('infinity') else ""