class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        dic  = defaultdict(int)
       
        ones = defaultdict(int)
        for i in matches:
            dic[i[0]] += 1
            
            ones[i[0]] += 1
            dic[i[1]] += 1
        ans = [[],[]]
        for i in dic:
            # print(i)
            if ones[i] == dic[i]:
                ans[0].append(i)
            elif ones[i] + 1 == dic[i]:
                ans[1].append(i)
        # print(dic,ones)
        ans[1].sort()
        ans[0].sort()
        return ans