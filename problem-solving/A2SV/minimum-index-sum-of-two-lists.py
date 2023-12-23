class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = defaultdict(lambda:-1)
        dic2 = defaultdict(lambda: -1)
        for i in range(len(list1)):
            dic1[list1[i]] = i
        for i in range(len(list2)):
            dic2[list2[i]] = i
        ans = []
        mx = len(list1) + len(list2)
        for key in dic1:
            if dic2[key]!= -1:
                if mx > (dic2[key] + dic1[key]):
                    mx = dic2[key] + dic1[key]
                    ans = []
                    ans.append(key)
                elif mx == (dic2[key] + dic1[key]):
                    ans.append(key)
        return ans