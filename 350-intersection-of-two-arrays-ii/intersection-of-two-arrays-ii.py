class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums2)
        arr = []
        for x in nums1:
            if counter[x] > 0:
                arr.append(x)
                counter[x] -= 1
        return arr