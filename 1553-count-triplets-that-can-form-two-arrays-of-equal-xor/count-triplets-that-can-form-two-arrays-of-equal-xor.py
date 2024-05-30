class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0]
        for i in arr:
            prefix.append(prefix[-1]^i)
        ans = 0
        for i in range(len(prefix)):
            for y in range(i+1,len(prefix)):
                left = prefix[i] ^ prefix[y]
                for j in range(y,len(arr)):
                    right = prefix[j+1]^prefix[y]
                    if right == left:
                        ans += 1
        return ans