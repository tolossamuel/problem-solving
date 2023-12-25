class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = []
        dic = defaultdict(lambda:0)
        for i in range(len(cpdomains)):
            s = cpdomains[i].split(" ")
            dot = s[1].split(".")
            for y in range(len(dot)):
                dic[".".join(dot[y:])] += int(s[0])
        for key in dic:
            ans.append(str(dic[key]) + " " + key)
        return ans
