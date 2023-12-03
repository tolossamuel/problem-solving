class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        arr = []
        for i in bank:
            n = list(i)
            m = n.count("1")
            if m >0:
                arr.append(m)
        if len(arr) <= 1:
            return 0
        if len(arr) == 2:
            return (arr[0]*arr[1])
        print(arr)
        sumOf = []
        for i in range(len(arr)-1):
            sumOf.append(arr[i]*arr[i+1])
        ans = sum(sumOf)
        return ans