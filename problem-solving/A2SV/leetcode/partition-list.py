# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ans = None
        left = None
        right = None
        temp = head
        while(temp):
            if temp.val >= x:
                if right == None:
                    ans = ListNode(temp.val)
                    right = ans
                else:
                    right.next = ListNode(temp.val)
                    right = right.next
            else:
                # print(temp.val)
                if ans == None:
                    
                    ans = ListNode(temp.val)
                    right = ans
                    left = ans
                elif left == None:
                    
                    left = ListNode(temp.val,ans)
                    ans = left
                else:
                    new = ListNode(temp.val,left.next)
                    # print(new.val,"=======")
                    left.next = new
                    left = left.next
                    if right.next:
                        right = right.next
                # print(left.val)
            temp = temp.next
        return ans

                    
