# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        temp = head
        while(temp):
            size += 1
            temp = temp.next
        remider = size%k
        index = size//k
        temp = head
        pos = head
        counter = index
        counter += 1 if remider > 0 else 0
        remider  -= 1 if remider > 0 else 0
        ans = []
        while(temp):
            if counter > 0:
                counter -= 1
            else:
                ans.append(pos)
                pos = temp
                counter = index
                counter += 1 if remider > 0 else 0
                remider  -= 1 if remider > 0 else 0
                counter -= 1
            if counter == 0:
                prev = temp
                temp = temp.next
                prev.next = None
            else:    
                temp = temp.next
        else:
            ans.append(pos)
        size +=1 if size == 0 else 0
        for i in range(size,k):
            ans.append(temp)

        return ans