class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0 
        types = collections.defaultdict(int)
        total = 0
        res = 0
        for i in range(len(fruits)):
            types[fruits[i]] += 1
            total += 1
            while(len(types)>2):
                f = fruits[left]
                types[f] -= 1
                left += 1
                total -= 1
                if not types[f]:
                    types.pop(f)
            res = max(res,total)
        # print(types)
        return res