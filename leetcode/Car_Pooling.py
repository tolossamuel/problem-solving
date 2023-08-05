class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: x[1])
        max_values = [sub_arr[2] for sub_arr in sorted_trips]
        max_value = max(max_values)
        heap_arr = [0]*(max_value)
        summ = 0
        for i in range(len(sorted_trips)):
            if summ > capacity :
                return False
            else:
                summ += sorted_trips[i][0]
                try:
                    if (heap_arr[sorted_trips[i][2]] != 0):
                        heap_arr[sorted_trips[i][2]] +=sorted_trips[i][0]
                    else:
                        heap_arr[sorted_trips[i][2]] =sorted_trips[i][0]
                except:
                    pass
                for i in range(sorted_trips[i][1]+1):
                    try:
                        if heap_arr[i] != 0:
                            summ -= heap_arr[i]
                            heap_arr[i] = 0
                    except:
                        pass
        if summ > capacity:
            return False
        return True

