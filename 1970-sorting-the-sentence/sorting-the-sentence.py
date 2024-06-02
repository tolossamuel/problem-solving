class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split(" ")
        def merge(arr,left,right):
            if left == right:
                return [arr[left]]
            mid = (left + right)//2
            left_side = merge(arr,left,mid)
            right_side = merge(arr,mid+1,right)
            ans = []
            l, r = 0, 0
            while(l < len(left_side) and r < len(right_side)):
                if left_side[l][-1] <= right_side[r][-1]:
                    ans.append(left_side[l])
                    l += 1
                else:
                    ans.append(right_side[r])
                    r += 1
            ans += left_side[l:]
            ans += right_side[r:]
            return ans
        ans = merge(l,0,len(l)-1)
        for i in range(len(ans)):
            ans[i] = ans[i][:len(ans[i])-1]
            
        return " ".join(ans)
    
