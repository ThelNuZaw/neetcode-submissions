class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        res = 1
        prev = ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and prev != ">":
                res = max(res, right - left + 1)
                right += 1
                prev = ">"
            elif arr[right - 1] < arr[right] and prev != "<":
                res = max(res, right - left + 1)
                right += 1
                prev = "<"
            else:
                right = right + 1 if arr[right - 1] == arr[right] else right
                left = right - 1
                prev = ""
        return res