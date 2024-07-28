class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def countSub(n):
            print(n)
            left = 0
            right = 0
            dic = defaultdict(int)
            sets = set()
            counter = 0
            while(right < len(nums) or len(sets) >= n):
                if len(sets) < n:
                    sets.add(nums[right])
                    dic[nums[right]] += 1
                    right += 1
                else:
                    counter += (len(nums) - right+1)
                    dic[nums[left]] -= 1
                    if dic[nums[left]] == 0:
                        sets.remove(nums[left])
                    left += 1
        
            return counter
        x =  countSub(k+1)
        y = countSub(k)

        return y - x
