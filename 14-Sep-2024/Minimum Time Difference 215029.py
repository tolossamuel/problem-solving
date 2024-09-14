# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # for i in range(len(timePoints)):
        #     left = timePoints[i].split(":")
        #     # print(left)
        #     if left[0] == "00":
             
        #         timePoints[i] = "24:"+left[1]
        timePoints.sort(reverse = True)
        ans = float("inf")
        print(timePoints)
        for i in range(1,len(timePoints)):
            right = timePoints[i-1].split(":")
            left = timePoints[i].split(":")
            h = int(right[0]) - int(left[0])
            m = (int(right[1]) - int(left[1]))
            # print(h,m)
            ans = min(ans,h*60 + m)
        right = timePoints[0].split(":")
        left = timePoints[-1].split(":")

        to_left = ((60* int(left[0])) + int(left[1]))
        to_right = (24 - int(right[0])) * 60 - int(right[1])

        ans = min(ans,to_left+to_right)
        return ans