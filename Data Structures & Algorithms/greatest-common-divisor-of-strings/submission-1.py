class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def isDivisor(l):
            if len1 % l != 0 or len2 % l != 0:
                return False
            t1, t2 = len1 // l, len2 // l
            return str1[:l] * t1 == str1 and str1[:l] * t2 == str2
                

        for l in range(min(len1, len2), 0 , -1):
            if isDivisor(l):
                return str1[:l]
        return ""