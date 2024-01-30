# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        temp = head
        count = 0
        new = None
        while(temp):
            if count % 2 == 0:
                odd.append(temp.val)
            else:
                even.append(temp.val)
            count += 1
            temp = temp.next
        if odd:
            new = ListNode(odd[-1])
            tail = new
        elif even:
            new = ListNode(even[-1])
            tail = new
        print(odd,even)
        for i in range(len(odd)-2,-1,-1):
            temp = ListNode(odd[i],new)
            new = temp
        x = 0 if odd else 1
        for i in range(x,len(even)):
            temp = ListNode(even[i])
            tail.next = temp
            tail = tail.next
        return new
