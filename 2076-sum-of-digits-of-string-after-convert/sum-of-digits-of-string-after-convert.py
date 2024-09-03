class Solution:
    def getLucky(self, s: str, k: int) -> int:
        arr =[]
        for x in s:
            arr.append(str(ord(x) - ord('a')+1))
        ans = 0
        arr = "".join(arr)

        arr = [int(x) for x in arr]
   
        for i in range(k):
            _sum = sum(arr)
            arr = []
            for x in str(_sum):
                arr.append(int(x))
        return _sum