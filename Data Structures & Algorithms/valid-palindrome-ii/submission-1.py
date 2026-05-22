class Solution:
    def validPalindrome(self, s: str) -> bool:
        clean = ''.join(filter(str.isalnum, s.lower()))
        left = 0
        right = len(clean) - 1
        while left < right:
            if clean[left] != clean[right]:
                skipLeft = clean[left+1:right + 1]
                skipRight = clean[left: right]
                return(skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1])
            left += 1
            right -= 1
        return True
        