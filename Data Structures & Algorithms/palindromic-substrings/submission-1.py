class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        #think like start at the middle and expand left and right
        #odd length
        for i in range(len(s)):
            count += self.countPali(s, i, i)
            count += self.countPali(s, i, i + 1)
        return count
        
    def countPali(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
            