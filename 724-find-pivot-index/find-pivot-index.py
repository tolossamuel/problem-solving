class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        [1,8,11,17,22,28]
        

        pref = [nums[0]]
        
        
        for i in range(1,len(nums)):
            pref.append(pref[-1]+nums[i])
        if len(pref) == 1:
            return 0
        for i in range(len(pref)):
            if i == 0:
                if pref[-1] - pref[i] == 0:
                    return 0
            elif i+1 == len(pref):
                if pref[-2] == 0:
                    return len(pref)-1
            elif pref[i-1] == (pref[-1]-pref[i]):
                return i
        return -1
       