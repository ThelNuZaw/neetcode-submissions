class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        else:
            su = sorted(s)
            tu = sorted(t)
            if(su == tu):
                return True
            else:
                return False
        