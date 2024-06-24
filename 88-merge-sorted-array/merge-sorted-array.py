class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        x = 0
        y = 0
        while(x < m and y < n):
            if nums1[x] < nums2[y]:
                ans.append(nums1[x])
                x += 1
            else:
                ans.append(nums2[y])
                y+=1
        ans += nums1[x:m]+nums2[y:n]
        nums1[:] = ans 
       