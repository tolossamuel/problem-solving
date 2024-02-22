class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[-1]]
        dic = {nums2[-1]:-1}
        for i in range(len(nums2)-2,-1,-1):
            if nums2[i] < stack[-1]:
                dic[nums2[i]] = stack[-1]
                stack.append(nums2[i])
            else:
                while(stack and stack[-1] <= nums2[i]):
                    stack.pop()
                if not stack:
                    dic[nums2[i]] = -1
                else:
                    dic[nums2[i]] = stack[-1]
                stack.append(nums2[i])
        ans = []
        for key in nums1:
            ans.append(dic[key])
        return ans