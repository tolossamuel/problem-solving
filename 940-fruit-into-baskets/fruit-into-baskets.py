class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        visited = set()
        ans = 0
        dic = defaultdict(int)
        
        while(right < len(fruits)):
            if len(visited) < 2 or (fruits[right] in visited):
                visited.add(fruits[right])
                dic[fruits[right]] += 1 
                right += 1
            else:
                
                dic[fruits[left]] -= 1
                if dic[fruits[left]] <= 0:
                    visited.remove(fruits[left])
                    dic.pop(fruits[left])
                left += 1
            ans = max(ans,(right - left))
            
        return ans