class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic = {n:0 for n in arr}
        for i in arr:
            dic[i] += 1
        m = len(arr)
        ans = 0
        persent = 0
        for key in dic:
            if (dic[key]*100)/m >= 25:
                if persent < ((dic[key]*100)/m):
                    ans = key
                    persent = (dic[key]*100)/m

        return ans
