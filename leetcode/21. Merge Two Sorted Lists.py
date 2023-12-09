# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def sortList(temp):
            
            temp1 = temp
            while( temp1.next):
                temp2 = temp1
                print(temp2.val)
                while(temp2):
                   
                    if temp1.val> temp2.val:
                       
                        temp1.val,temp2.val = temp2.val,temp1.val
                    temp2 = temp2.next
                temp1 = temp1.next
            return temp
        if list1:
            
            temp = list1
            while(temp.next):
                temp = temp.next
                
            if list2:

                temp.next = list2
             
            
            return (sortList(list1))
        else:
            return list2
            

            