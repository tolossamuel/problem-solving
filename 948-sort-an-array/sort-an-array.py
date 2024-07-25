class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                left_value = merge_sort(arr[:mid])
                right_value = merge_sort(arr[mid:])

                l = 0
                r = 0
                k = 0
                ans = []
                while(l < len(left_value) and r < len(right_value)):
                    if left_value[l] <= right_value[r]:
                        arr[k] = left_value[l]
                        l += 1
                    else:
                        arr[k] = right_value[r]
                        r += 1
                    k += 1
                while(l < len(left_value) and k < len(arr)):
                    arr[k] = left_value[l]
                    l += 1
                    k += 1
                while(r < len(right_value) and k < len(arr)):
                    arr[k] = right_value[r]
                    r += 1
                    k += 1
                return arr
            else:
                return arr
        merge_sort(nums)
        return nums

