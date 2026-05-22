class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #make sure the total gas is not less than total cost to travel
        # then the problem is unique so it has only one possible ans
        if(sum(gas) < sum(cost)):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start