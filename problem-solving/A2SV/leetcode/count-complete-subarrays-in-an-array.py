class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = 0
        checker = len(set(nums))
        n = len(nums)
        print(checker)
        for i in range(len(nums)):
            temp = set()
            for y in range(i,len(nums)):
                temp.add(nums[y])
                # print(temp)
                if len(temp) == checker:
                    counter += (n - y)
                    # print(123)
                    break
        return counter