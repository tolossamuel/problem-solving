class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [nums[0]]
        suf = deque()
        suf.appendleft(nums[-1])
        for i in range(1,len(nums)):
            pref.append(nums[i]*pref[-1])
        for i in range(len(nums)-2,-1,-1):
            suf.appendleft(nums[i]*suf[0])
        ans = []
        for i in range(len(pref)):
            if i +1 < len(suf) and i == 0:
                ans.append(suf[i+1])
            elif i > 0 and i +1 < len(suf):
                ans.append(suf[i+1]*pref[i-1])
            else:
                ans.append(pref[i-1])
        return ans