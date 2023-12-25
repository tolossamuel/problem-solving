class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for i in paths:
            m = i.split(" ")
            r= m[0]
            print(r)
            for i in range(1,len(m)):
                s = m[i].split("(")
              
                dic[s[1]].append(r +"/"+s[0])

        ans = []
        for key in dic:
            if len(dic[key]) >1:
                # print(dic[key])
                ans.append(dic[key])
                # print(ans)
        return ans

