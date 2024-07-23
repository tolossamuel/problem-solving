class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash = Counter(nums)
        new = defaultdict(list)
        for x,y in hash.items():
            new[y] += [x]*y
        ans = []
        x = list(new.keys())
        x.sort()
        for y in x:
            ans += sorted(new[y], reverse = True)
        return ans