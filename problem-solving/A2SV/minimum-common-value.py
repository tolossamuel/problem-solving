class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums1:
            dic[i] = 1
        ans = 11e9
        for i in nums2:
            if i in dic:
                ans  = min(ans,i)
        if ans == 11e9:
            return -1
        return ans