from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        event = []
        for x,y,h in buildings:
            event.append([x,h,0])
            event.append([y,h,1])
        event.sort()
        points = SortedList([0])
        i = 0
        ans = []
        # print(event)
        while(i < len(event)):
            x,h,t = event[i]
            if t == 0:
                points.add(h)
            else:
                points.remove(h)
            # print(points)
            if ans and ans[-1][0] == x and ans[-1][1] < h:
                ans.pop()
            if not ans or (ans[-1][-1] != points[-1] and points[-1] != 0):
                ans.append([x,points[-1]])
            elif points[-1] == 0 and ((i+1) == len(event)):
                ans.append([x,points[-1]])
            elif points[-1] == 0 and (event[i+1][0] > x):
                ans.append([x,points[-1]])
            i += 1
        return ans

        