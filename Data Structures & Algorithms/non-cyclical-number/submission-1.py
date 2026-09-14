class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            total = 0
            while n:
                digit = n % 10
                total += digit **2
                n = n // 10
            return total 
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
            if n == 1:
                return True
        return False

        
