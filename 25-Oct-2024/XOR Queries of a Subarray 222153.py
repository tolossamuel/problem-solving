# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        ans = []
    
        for x,y in queries:
            if x == 0:
                ans.append(arr[y])
            else:
                
                ans.append(arr[x-1] ^ arr[y])
     
        return ans