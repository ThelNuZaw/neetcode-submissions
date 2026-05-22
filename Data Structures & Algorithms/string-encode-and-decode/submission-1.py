class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        parts = []
        for strings in strs:
            count = len(strings)
            par = str(count)+"#"+strings
            parts.append(par)
        s = "".join(parts)
        return(s)

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s): # handle the length
            j = i # read the string
            while s[j] != '#': # read number until #
                j += 1
            num = int(s[i:j]) #extract the number
            word = s[j + 1 : num + j + 1]
            out.append(word)
            i = num + j + 1
        return(out)




