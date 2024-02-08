class Solution:
    def numberOfWays(self, s: str) -> int:
        dic = defaultdict(int)
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                dic["10"] += dic["0"]
                dic["1"] += 1
                dic["101"] += dic["01"]
            else:
                dic["0"] += 1
                dic["01"] += dic["1"]
                dic["010"] += dic["10"]
        # print(dic)
        return (dic["010"] + dic["101"])