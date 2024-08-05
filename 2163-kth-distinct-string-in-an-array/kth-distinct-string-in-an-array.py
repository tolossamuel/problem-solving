class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash = Counter(arr)
        counter = 0
        first = ''
        for key in arr:
            if hash[key] == 1:
                counter += 1
                if counter == k:
                    first = key 
        return first
        
