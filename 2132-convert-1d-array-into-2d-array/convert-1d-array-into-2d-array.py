class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m * n != len(original)):
            return []
        ans =[]
        counter = 0
        temp = []
        for x in original:
            counter += 1
            temp.append(x)
            if counter == n:
                ans.append(temp)
                temp = []
                counter = 0
        if temp:
            ans.append(temp)
        return ans