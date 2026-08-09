class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq_map = {}
        for h in hand:
            freq_map[h] = 1 + freq_map.get(h, 0)
        
        minheap = list(freq_map.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]

            for i in range(first, first + groupSize):
                if i not in freq_map:
                    return False
                freq_map[i] -= 1
                if freq_map[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True