class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1 += ["0"] * ( max(len(v1),len(v2)) - len(v1))
        v2 += ["0"] * (max(len(v1),len(v2)) - len(v2))
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
        return 0