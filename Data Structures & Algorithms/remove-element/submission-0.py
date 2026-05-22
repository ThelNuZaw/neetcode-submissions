class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = []
        for n in nums:
            if n == val:
                continue
            k.append(n)
        for i in range(len(k)):
            nums[i] = k[i]
        return len(k)

               