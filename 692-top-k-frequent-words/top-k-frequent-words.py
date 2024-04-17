class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        dic2 = defaultdict(list)
        for i in dic:
            dic2[dic[i]].append(i)
        for key in dic2:
            dic2[key] = sorted(dic2[key])
        heap = list(dic2.keys())
        heap = [-x for x in heap]
        heapify(heap)
        ans = []
        while(k>0):
            x = -heappop(heap)
            pos = min(k,len(dic2[x]))
            ans += dic2[x][:pos]
            k -= pos
        # print(ans)
        return ans