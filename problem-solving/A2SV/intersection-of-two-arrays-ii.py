class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for i in nums1:
            dic[i] += 1
        ans = []
        for i in range(len(nums2)):
            if dic[nums2[i]]!= 0:
                ans.append(nums2[i])
                dic[nums2[i]] -= 1
        return ans
        
        