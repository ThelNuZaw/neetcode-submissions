class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # for n in nums:
        #    count[n] = count.get(n,0) + 1
        # return max(count,key=count.get)

        count = defaultdict(int)
        maxcount = ans = 0
        for n in nums:
            count[n] += 1
            if count[n] > maxcount:
                maxcount = count[n]
                ans = n
        return ans