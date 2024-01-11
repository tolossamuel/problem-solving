class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        ans = 0
        left = 0
        right = 0
        count = 0
        sum_of = []
        while(right < len(nums)):
            if dic[nums[right]] and dic[nums[right]][1] >= left:
                count += nums[right]
                sum_of.append(count)
                if left == 0:
                    ans = max(ans,sum_of[right-1])
                else:
                    ans = max(ans,sum_of[right-1]-sum_of[left-1])
                left = dic[nums[right]][1]+1
                dic[nums[right]] = [1,right]
            else:
                count += nums[right]
                dic[nums[right]] = [1,right]
                sum_of.append(count)
            right += 1
        if left > 0:
            ans = max(ans,sum_of[right-1] - sum_of[left-1])
        else:
            ans = max(ans,sum_of[right-1])
        return ans
                