class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(filter(str.isalnum, s.lower()))
        left, right = 0, len(clean)-1
        isPair = True
        while left < right and isPair:
            if(clean[left] == clean[right]):
                left +=1
                right -= 1
                
            else:
                isPair = False
        return isPair
        