class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect.bisect_left(arr,x)
        left = index
        right = index
        if left < len(arr) and (arr[left] == x):
            right += 1
            left -= 1
        while((right - left) <= k):
            if right >= len(arr):
                left -= 1
            elif left < 0:

                right += 1
            elif (x- arr[left] ) > (arr[right] - x):
                right += 1
            else:
                left -= 1
            
        ans = arr[left+1:right] 
        return ans