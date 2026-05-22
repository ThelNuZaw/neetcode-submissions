class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        ctr = Counter(nums)
        l = []
        for k, v in ctr.items():
            if v > len(nums)/3:
                l.append(k)
    
        return l