class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for n1 in range(len(num1)):
            for n2 in range(len(num2)):
                digit = int(num1[n1]) * int(num2[n2])

                res[n1 + n2] += digit #adding multiplication result to whatever calculated in previous step at this index
                res[n1 + n2 + 1] += (res[n1 + n2] // 10) # carry
                res[n1 + n2] = res[n1 + n2] % 10

        res = res[::-1]
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1 #remove leading zeroes

        res = map(str, res[beg:])
        return "".join(res)
