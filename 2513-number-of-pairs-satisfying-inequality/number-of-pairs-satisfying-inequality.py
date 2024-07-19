
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        new_arr = []
        for i in range(len(nums1)):
            new_arr.append(nums1[i] - nums2[i])
        counter = 0
        def merges_sort(left,right,arr):
            nonlocal counter
            if left == right:
                return [new_arr[left]]
            mid = left + (right - left)//2
            left_side = merges_sort(left,mid,arr)
            right_side = merges_sort(mid+1,right,arr)
            i,j = 0,0
            while(i < len(left_side) and j < len(right_side)):
                if left_side[i] <= (right_side[j] + diff):
                    counter += (len(right_side) - j)
                    i += 1
                else:
                    j += 1
            return sorted(left_side,right_side)
        def sorted(left_side,right_side):
            x,y = 0, 0
            ans = []
            while(x < len(left_side) and y < len(right_side)):
                if left_side[x] < right_side[y]:
                    ans.append(left_side[x])
                    x += 1
                else:
                    ans.append(right_side[y])
                    y += 1
            ans += left_side[x:].copy()
            ans += right_side[y:].copy()
            return ans
        merges_sort(0,len(new_arr)-1,new_arr)
        return counter