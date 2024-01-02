class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def helper(arr,end):
            start = 0
            while(start < end):
                arr[start],arr[end] = arr[end],arr[start]
                start += 1
                end -= 1
        n = len(arr)
        ans = []
        for i in range(n,0,-1):
            index = arr.index(max(arr[:i]))
            if index != 0:
                helper(arr,index)
                ans.append(index+1)
            helper(arr,i-1)
            ans.append(i)
        return ans
            