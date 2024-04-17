class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        events = [0]*n
        used = []
        available  = list(range(n))
        meetings.sort()
        
        for start, end in meetings:
            while(used and start >= used[0][0]):
                _,room = heapq.heappop(used)
                heapq.heappush(available, room)
            if not available:
                end_time , room = heapq.heappop(used)
                end = end_time + (end-start)
                heapq.heappush(available,room)
            room = heapq.heappop(available)
            heapq.heappush(used,(end,room))
            events[room] += 1
        return events.index(max(events))
