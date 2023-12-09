# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            print("no list")
            return None
        
       
        for i in range(len(lists)):
            if lists[i]:
                index = i
                temp = lists[i]
                head = lists[i]
                break
        else:
            return None
        while(temp.next):
            temp = temp.next
            
        for i in range(index+1,len(lists)):
            if lists[i]:
                temp.next = lists[i]
                temp = temp.next
                while(temp.next):
                    temp = temp.next
        def sorts(node):

            if not node:
                return []
            temp = node
            index = node
            while(temp.next):
                index = temp
                while(index):
                    if temp.val > index.val:
                        temp.val,index.val = index.val, temp.val
                    index = index.next
                temp = temp.next
            return node
        head = sorts(head)
        
        return (head)
        