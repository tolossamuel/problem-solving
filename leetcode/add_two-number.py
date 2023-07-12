# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=l1
        temp2=l2
        c=[]
        d=[]
        i=0
        while temp is not None:
            c.insert(0,str(temp.val))
            temp=temp.next
            i+=1
        i=0
        while temp2 is not None:
            d.insert(0,str(temp2.val))
            temp2=temp2.next
            i+=1
        c=''.join(c)
        d=''.join(d)
        d=int(d)
        c=int(c)
        d+=c
        d=str(d)
        d=list(d)
        d.reverse()
        d=''.join(d)
        temp3=l1
        for i in range(len(d)):
            temp3.val=int(d[i])
            if temp3.next==None:
                temp3.next=l2
            if i<len(d)-1:
                temp3=temp3.next
        temp3.next=None
        
        return l1    