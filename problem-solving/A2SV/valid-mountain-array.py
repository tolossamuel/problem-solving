class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        left = 0
        right = len(arr) -1
     
        while(left < len(arr)-1 and arr[left] < arr[left+1]):
            left += 1
        while (right > 0 and arr[right] < arr[right-1]):
            right -= 1
        if left == 0 or right == len(arr)-1 or (left != right):
            return False
        
        return True