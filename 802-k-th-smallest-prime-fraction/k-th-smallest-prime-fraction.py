class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        com = []
        for i in range(len(arr)-1):
            for y in range(i+1,len(arr)):
                com.append([arr[i]/arr[y],[arr[i],arr[y]]])
        com.sort()
        return com[k-1][1]