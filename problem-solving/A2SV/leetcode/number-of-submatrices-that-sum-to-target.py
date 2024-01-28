class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pref = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        # pref[0][0] = matrix[0][0]
        n = len(pref)
        m = len(pref[0])
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                pref[i][j] = matrix[i-1][j-1] + pref[i][j-1] + pref[i-1][j] - pref[i-1][j-1]
        counter = 0
        print(pref)
        for y in range(1,len(matrix)+1):
            for y2 in range(y,len(matrix)+1):
                dic = defaultdict(int)
                dic[0] += 1
                for x in range(1,len(matrix[0])+1):
                    _sum = pref[y2][x] - pref[y-1][x]
                    dif = _sum - target
                    counter += dic[dif]
                    dic[_sum ] += 1

                # print("========")
        return counter
                        
