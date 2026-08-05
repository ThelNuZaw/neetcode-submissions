class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)] #minheap [0 - n-1] for meeting room
        used = [] #(end time, room)
        count = [0] * n

        for start, end in meetings:
            #meeting is finished and next start time is greater than prev meeting end
            while used and start >= used[0][0]:
                _, room_num = heapq.heappop(used)
                heapq.heappush(available, room_num)
            
            #room is not available for any meetings
            if not available:
                end_time, room_num = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room_num)

            room_num = heapq.heappop(available)
            heapq.heappush(used, (end, room_num))
            count[room_num] += 1
        return count.index(max(count))