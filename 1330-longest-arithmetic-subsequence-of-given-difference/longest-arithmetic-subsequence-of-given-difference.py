class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        visited = {}
        ans =[0] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            x = arr[i] + difference
            
            if x in visited:
                ans[i] = visited[x]
            ans[i] += 1
     
            if arr[i] in visited:
                visited[arr[i]] = max(visited[arr[i]],ans[i])
            else:
                visited[arr[i]] = ans[i]
        return max(ans)
