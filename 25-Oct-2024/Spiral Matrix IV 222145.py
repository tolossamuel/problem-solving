# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        n,m = m,n
        arr = [[-1 for _ in range(m)] for _ in range(n)]

        x = 0
        y = 0
        dir = 0
        temp = head
        if not temp.next:
            arr[0][0] = temp.val
            return arr
        while(temp):
        
            if dir == 0:
                if arr[x][y] == -1:
                    arr[x][y] = temp.val
                if(y+1<m and arr[x][y+1] == -1):
                    y += 1
                    temp = temp.next
                else:
                    if not temp.next:
                        break
                    dir = 1
            elif dir == 1:
                if arr[x][y] == -1:
                    arr[x][y] = temp.val
                if (x+1 < n and arr[x+1][y] == -1):
                    x += 1
                    temp = temp.next
                else:
                    if not temp.next:
                        break
                    dir = 3
            elif dir == 2:
                if arr[x][y] == -1:
                    arr[x][y] = temp.val
                if (x-1 >= 0 and arr[x-1][y] == -1):
                    x -= 1
                    temp = temp.next
                else:
                    if not temp.next:
                        break
                    dir = 0
            elif dir == 3:
                if arr[x][y] == -1:
                    arr[x][y] = temp.val
                if (y-1 >= 0 and arr[x][y-1] == -1):
                    y -= 1
                    temp = temp.next
                else:
                    if not temp.next:
                        break
                    dir = 2

        return arr