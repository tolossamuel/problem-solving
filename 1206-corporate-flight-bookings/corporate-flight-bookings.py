class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref = [0]*n
        for i in bookings:
            pref[i[0]-1] += i[2]
            if i[1] < len(pref):
                pref[i[1]] += -i[2]


        for i in range(1,n):
            pref[i] += pref[i-1]
        return pref