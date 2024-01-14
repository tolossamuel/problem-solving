class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        stack = deque()
        temp = 0
        dic = {}
        ans = 0
        while(right < len(fruits)):
            if fruits[right] in stack:
                # print(123)
                temp += 1
                dic[fruits[right]] = right
                right += 1

                # print(right)
            elif len(stack) <= 1:
                stack.append(fruits[right])
                dic[fruits[right]] = right
                right += 1
                temp += 1
            else:
                ans = max(ans,temp)
                print(dic[fruits[left]])
                left  = min(dic[stack[0]],dic[stack[1]])+1
                stack = []
                right = left
                temp = 0
        # print(temp)
        ans = max(ans,temp)
        return ans