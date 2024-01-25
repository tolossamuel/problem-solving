class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        x = 0
        for i in trips:
            x = max(x,i[2])
        pref = [0]*(x+1)
        for i in trips:
            pref[i[1]] += i[0]
            if i[2] < len(pref):
                pref[i[2]] += -i[0]
        # print(pref)
        if pref[0] > capacity:
            return False
        for i in range(1,len(pref)):
            pref[i] += pref[i-1]
            if pref[i] > capacity:
                return False
        return True