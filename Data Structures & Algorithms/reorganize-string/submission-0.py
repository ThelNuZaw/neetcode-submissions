class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-c, char] for char, c in count.items()]
        heapq.heapify(maxheap)

        res = ""
        prev = None
        while maxheap or prev:
            if prev and not maxheap: # waiting to get the prev but there is nothing in heap to process
                return ""
            c, char = heapq.heappop(maxheap)
            c += 1
            res += char

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if c != 0:
                prev = [c, char]
        return res