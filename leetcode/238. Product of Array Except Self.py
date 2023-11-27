class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [1,2,6,24]
        # [4,12,24,1]
        
        pre =[nums[0]]
        suf = [nums[-1]]
        for i in range(len(nums)-1):
            pre.append(pre[i]*nums[i+1])
            suf.insert(0,(suf[0]*nums[len(nums)-2-i]))
        for i in range(len(nums)):
            if i == 0:
                nums[i] = suf[i+1]
            elif i + 1 == len(nums):
                nums[i] = pre[i-1]
            else:
                nums[i] = pre[i-1]*suf[i+1]
            
        return nums