class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        ans = []
        while(left < len(word1) and right < len(word2)):
            if word1[left] > word2[right]:
                ans.append(word1[left])
                left +=1
            elif word2[right] > word1[left]:
                ans.append(word2[right])
                right += 1
            else:
                for i in range(1,min(len(word1)-left, len(word2)-right)):
                    if word1[left+i] > word2[right+i]:
                        ans.append(word1[left])
                        left += 1
                        break
                    elif word1[left+i] < word2[right+i]:
                        ans.append(word2[right])
                        right += 1
                        break
                else:
                    if (len(word1)-left) > (len(word2)-right):
                        ans.append(word1[left])
                        left += 1
                    else:
                        ans.append(word2[right])
                        right += 1
                       
                    # print(ans)
                # print(ans)
        ans = "".join(ans) + word1[left:]+word2[right:]
        return ans