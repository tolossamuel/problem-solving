class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = str(num)
        x = list(x)
        x.sort()
        x = "".join(x)
        # print(x)
        x = "".join(x)
        # print(x)

        l = 0
        r = 0
        for i in range(len(x)):
            if i %2 == 0:
                l *= 10
                l += int(x[i])
            else:
                r *= 10
                r += int(x[i])
        # print(l),
        # print(r)
        return (l+r)
