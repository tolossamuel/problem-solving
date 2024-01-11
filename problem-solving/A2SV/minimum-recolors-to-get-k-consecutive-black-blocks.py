class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0 
        ans = float("inf")
        counter = 0
        change = 0
        while(right < len(blocks)):
            if blocks[right] == "W":
                change += 1
            counter += 1
            right += 1
            
            if counter == k:
                ans = min(change,ans)
                if blocks[left] == "W":
                    change -= 1
                left += 1
                counter -= 1
        return ans