class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for i in strs:
            x = list(i)
            x.sort()
            x = "".join(x)
            dic[x].append(i)
        ans = []
        for key in dic:
            ans.append(dic[key])


            
        return ans